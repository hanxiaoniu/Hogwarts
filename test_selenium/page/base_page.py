#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/25 11:09 下午
# @Author: chloehan
# @File  : base_page.py
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

"""完成对通用代码的引入,初始化方法、公共逻辑等"""


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            # 允许每个类定义自己的页面地址
            self._driver.get(self._base_url)
        else:
            self._driver = driver

    def close(self):
        time.sleep(15)
        """
        初始化之后在其它地方调用不到driver的具体方法（初始化方法为None类型,所以要进行改造，使用remote的webDriver）
        """
        self._driver
