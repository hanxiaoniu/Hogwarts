#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/1 10:31 上午
#@Author: chloehan
#@File  : test_search.py

class TestSearch:
    def setup(self):
        self.main = App.start().main()

    def test_search(self):
        self.main.goto_search_page()