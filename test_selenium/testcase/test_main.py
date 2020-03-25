#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/24 11:32 下午
#@Author: chloehan
#@File  : test_main.py
from test_selenium.page.main import Main
class TestMain:
    def test_add_member(self):
        main=Main()
        main.add.member().add_member("xxx")
        assert "aaa" in main.import_user()