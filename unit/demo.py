#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/2 9:32 下午
# @Author: chloehan
# @File  : demo.py
""" test fixture 装置，预置操作
    test case 用例
    test suite 套件，设定测试用例顺序，容纳case的容器
    test runner 运行 构建执行流程
"""


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def setup_module():
    print("setup_module")


def setup_function():
    print("setup_function")


class TestClass:
    def setup(self):
        print("setup")

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
