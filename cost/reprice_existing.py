"""Tính lại dự toán từ simulate-2 đã chạy; không gọi API, không sửa kết quả cũ.

Chạy: python cost/reprice_existing.py
"""
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cost"))
import simulate


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def market_scenarios():
    # Mốc 12 triệu năm 2023 của Vietdata; không phải MAU hoặc thị phần sản phẩm.
    anchor, x, n, z = 12_000_000, 13, 22, 1.959963984540054
    p = x / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return {
        "anchor": anchor, "x": x, "n": n, "ratio": p,
        "low_ratio": center - half, "high_ratio": center + half,
        "users": {"low": round(anchor * (center - half)),
                  "base": round(anchor * p), "high": round(anchor * (center + half))},
    }


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sim_path = ROOT / "cost/simulate-2.csv"
    eval_path = ROOT / "eval/run-2.csv"
    traces = [ROOT / "traces/simulate-2.jsonl", ROOT / "traces/run-2.jsonl"]
    before = {str(p.relative_to(ROOT)): digest(p) for p in [sim_path, eval_path, *traces]}
    with sim_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) < 50 or len({r["session"] for r in rows}) != len(rows):
        raise ValueError("Cần ít nhất 50 phiên có mã riêng")
    if any(r["error"] for r in rows):
        raise ValueError("Có phiên lỗi; phải nêu rõ trước khi dùng")
    for r in rows:
        for k in ("turns", "tokens_in", "tokens_out", "model_calls", "tool_calls"):
            r[k] = int(r[k])
        r["latency_s"] = float(r["latency_s"])
        r["by_model"] = json.loads(r["tokens_by_model"])
        if sum(v["in"] for v in r["by_model"].values()) != r["tokens_in"]:
            raise ValueError("Token vào không khớp phần theo model")
        if sum(v["out"] for v in r["by_model"].values()) != r["tokens_out"]:
            raise ValueError("Token ra không khớp phần theo model")
    models = simulate.measured_models(rows)
    graded, _ = simulate.pick_rate(models, str(eval_path))
    if models != ["deepseek-flash"] or graded["models"] != models:
        raise ValueError("Mô phỏng và run-2 phải cùng deepseek-flash")
    if sum(r["tokens_in"] + r["tokens_out"] for r in rows) <= 0:
        raise ValueError("Không có token đo thật")
    cfg, warnings = simulate.load_config()
    market = market_scenarios()
    if any(cfg["users"][k] != v for k, v in market["users"].items()):
        raise ValueError("users trong YAML không khớp công thức quy mô")
    rate = graded["passed"] / graded["total"]
    per_model = {}
    total_share = sum(p["share"] for p in cfg["personas"])
    for price in cfg["prices"]:
        def cost(r):
            return (r["tokens_in"] * price["input"] + r["tokens_out"] * price["output"]) / 1e6
        session_cost = sum(cost(r) for r in rows) / len(rows)
        persona_cost = {}
        for p in cfg["personas"]:
            part = [r for r in rows if r["persona"] == p["name"]]
            if not part:
                raise ValueError("Persona không được lấy mẫu")
            persona_cost[p["name"]] = sum(cost(r) for r in part) / len(part)
        monthly_per_user = sum(p["share"] / total_share * p["uses_per_month"] *
                               persona_cost[p["name"]] for p in cfg["personas"])
        per_model[price["model"]] = {
            "per_session": session_cost,
            "per_success_proxy": session_cost / rate,
            "per_user_month": monthly_per_user,
            "monthly": {k: v * monthly_per_user for k, v in market["users"].items()},
        }
    report = {
        "mode": "reprice_existing_no_api_calls",
        "simulation_run_id": rows[0]["run_id"], "sessions": len(rows), "errors": 0,
        "measured_models": models, "tokens_in": sum(r["tokens_in"] for r in rows),
        "tokens_out": sum(r["tokens_out"] for r in rows),
        "eval_run_id": graded["run_id"], "passed": graded["passed"],
        "total": graded["total"], "rate": rate, "market": market,
        "models": per_model, "warnings": warnings, "immutable_sha256": before,
    }
    md = ["# Tính lại giá từ simulate-2 đã có", "",
          "Không gọi API; không phải lượt simulate mới. Giữ nguyên CSV và trace gốc.", "",
          *simulate.summarize(cfg, rows, graded), ""]
    (ROOT / "cost/reprice-simulate-2.md").write_text("\n".join(md), encoding="utf-8")
    (ROOT / "cost/reprice-simulate-2.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if any(digest(ROOT / p) != value for p, value in before.items()):
        raise ValueError("Tệp kết quả gốc đã thay đổi")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
