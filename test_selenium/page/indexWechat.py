#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/25 10:18 下午
# @Author: chloehan
# @File  : indexWechat.py
from selenium.webdriver.common.by import By
from selenium import webdriver

from test_selenium.page.base_page import BasePage
from test_selenium.page.register import Register


class Index(BasePage):
    _base_url="https://work.weixin.qq.com/"

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        return Register(self.driver)
