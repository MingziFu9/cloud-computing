"""实验 5-1：部署到函数计算的第一个函数。

阿里云函数计算（Python 运行时）调用 handler(event, context)：
event 是触发函数时传入的数据（字节串），context 是运行环境信息。
本函数接收 {"price_per_hour": 0.5, "hours_per_day": 4}，返回按量付费一个月的费用。
"""
import json
import time

COLD_START_AT = time.time()   # 这行只在函数实例第一次启动（冷启动）时执行


def handler(event, context):
    start = time.time()
    try:
        data = json.loads(event or b"{}")
    except ValueError:
        data = {}
    price = float(data.get("price_per_hour", 0.5))
    hours = float(data.get("hours_per_day", 24))
    result = {
        "monthly_cost": round(price * hours * 30, 2),
        "instance_age_seconds": round(start - COLD_START_AT, 1),   # 实例存活了多久：每次都接近 0 说明每次都是冷启动
        "duration_ms": round((time.time() - start) * 1000, 3),
    }
    return json.dumps(result, ensure_ascii=False)


if __name__ == "__main__":
    # 在本机模拟两次调用，验证函数逻辑
    print(handler(b'{"price_per_hour": 0.5, "hours_per_day": 4}', None))
    time.sleep(1)
    print(handler(b'{"price_per_hour": 0.5, "hours_per_day": 24}', None))
