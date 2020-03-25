#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/24 11:22 下午
#@Author: chloehan
#@File  : test_contect.py
from test_selenium.page import Contect


class TestConst:
    def test_add_member(self):
        contact=Contect()
        contact.add_member("xxx")
        contact
