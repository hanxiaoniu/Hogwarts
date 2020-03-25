#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/25 11:09 下午
#@Author: chloehan
#@File  : base_page.py
from selenium import webdriver

"""完成对通用代码的引入,初始化方法等"""
class BasePage:
    def __init__(self, driver=None):
        if driver == None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            # 允许每个类定义自己的页面地址
            self.driver.get(self.base_url)
        else:
            self.driver = driver