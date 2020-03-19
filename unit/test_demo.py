#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/3 9:18 下午
# @Author: chloehan
# @File  : test_demo.py
import unittest


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    def setUp(self) -> None:
        print("setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def tearDown(self) -> None:
        print("teardown")

    def test_sum(self):
        print("testsum")
        x = 1 + 2
        print(x)
        self.assertEqual(4, x, f'x={x} expection =3')

    def test_demo(self):
        print("testdemo")
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
