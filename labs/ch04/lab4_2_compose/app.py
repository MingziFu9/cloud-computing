"""实验 4-2：一个最小的 Web 应用，用 Redis 记录页面被访问的次数。"""
import os
import socket

import redis
from flask import Flask

app = Flask(__name__)
# 主机名 redis 就是 docker-compose.yml 里的服务名，Compose 会自动把它解析成 Redis 容器的地址
cache = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)


@app.route("/")
def hello():
    count = cache.incr("hits")
    return (f"<meta charset='utf-8'><h1>你好，云计算！</h1>"
            f"<p>本页已被访问 {count} 次。</p>"
            f"<p>处理本次请求的容器：{socket.gethostname()}</p>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
