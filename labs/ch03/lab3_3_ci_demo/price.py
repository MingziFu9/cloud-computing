"""实验 3-3 的示例程序：按量付费的云服务器费用计算。"""


def monthly_cost(price_per_hour: float, hours_per_day: float, days: int = 30) -> float:
    """按量付费一个月的费用（元），保留两位小数。"""
    if price_per_hour < 0 or not 0 <= hours_per_day <= 24:
        raise ValueError("单价不能为负，每天使用时长应在 0～24 小时之间")
    return round(price_per_hour * hours_per_day * days, 2)


def cheaper_plan(price_per_hour: float, hours_per_day: float, monthly_price: float) -> str:
    """比较按量付费和包年包月，返回更省钱的方式。"""
    return "按量付费" if monthly_cost(price_per_hour, hours_per_day) < monthly_price else "包年包月"
