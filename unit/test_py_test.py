#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/3 10:19 下午
# @Author: chloehan
# @File  : test_py_test.py

# 课间作业
import pytest
import allure
import time
import os


def div(a, b):
    return a / b


@allure.suite('int数据组')
@pytest.mark.int
@pytest.mark.parametrize("number1,number2,expect0", {
    (10, 5, 2),
    (0, 1, 0),
    (3, 3, 1),
    (-3, 3, -1),
    (3, -3, -1),
})
def test_div_int(number1, number2, expect0):
    assert div(number1, number2) == expect0


@allure.suite('float数据组')
@pytest.mark.float
@pytest.mark.parametrize("number3,number4,expect1", {
    (2.33, 1, 2.33),
    (6.66, 2.22, 3),
    (2.22222222, 2, 1.111111)
})
def test_div_float(number3, number4, expect1):
    assert div(number3, number4) == expect1


@allure.suite('error数据组')
@pytest.mark.expection
@pytest.mark.parametrize("number5,number6,exception0", {
    (1, 0, 'ZeroDivisionError'),
    (1, 0, None)
})
def test_div_Zeroexception(number5, number6, exception0):
    with pytest.raises(eval(exception0)):
        div(number5, number6)


@allure.suite('TypeError数据组')
@pytest.mark.error
@pytest.mark.parametrize("number7,number8,exception1", {
    (3, 'a', 'TypeError'),
    ('a', 3, 'TypeError')
})
def test_div_exception(number7, number8, exception1):
    with pytest.raises(eval(exception1)):
        div(number7, number8)


if __name__ == '__main__':
    # 清空allure_results文件夹，清理掉allure历史记录
    for i in os.listdir(r'unit/allure_results'): os.remove('unit/allure_results/{}'.format(i))
    time.sleep(1)

    # 执行测试并保存allure需要的结果
    # pytest --junitxml=unit/junit.xml --alluredir=unit/allure_results  unit/
    os.system('pytest -v --alluredir=unit/allure_results {}'.format(__file__))
    time.sleep(1)

    # 使用allure展示测试报告
    os.system(r'allure serve unit/allure_results ')