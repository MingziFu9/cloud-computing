"""实验 3-3 的单元测试：每次提交代码，GitHub Actions 都会自动运行这些测试。"""
import pytest

from price import cheaper_plan, monthly_cost


def test_monthly_cost():
    assert monthly_cost(0.5, 24) == 360.0
    assert monthly_cost(0.5, 4) == 60.0


def test_cheaper_plan():
    assert cheaper_plan(0.5, 4, 200) == "按量付费"
    assert cheaper_plan(0.5, 24, 200) == "包年包月"


def test_bad_input():
    with pytest.raises(ValueError):
        monthly_cost(0.5, 25)
