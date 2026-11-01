# 与教材 4.1.3.3 的 Dockerfile 相同，只把基础镜像换成仍在维护的 Python 3.12
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python", "app.py"]
