FROM python:3.11-slim

WORKDIR /app

# Không cần pip install — codebase và web server dùng 100% thư viện chuẩn Python
COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

EXPOSE 8080

CMD ["python", "server.py"]
