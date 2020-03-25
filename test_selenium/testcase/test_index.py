#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/25 10:18 下午
# @Author: chloehan
# @File  : test_index.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_selenium.page.indexWechat import Index


class TestIndex:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/")

    def test_register(self):
        index = Index(self.driver)
        index.goto_register().register("chloehanmin","hanmin")

        # self.driver.find_element(By.LINK_TEXT,'立即注册').click()
        # self.driver.find_element(By.ID,"corp_name").send_keys("chloehanmin")
        # self.driver.find_element(By.ID,"manager_name").send_keys("hanmin")
        # self.driver.find_element(By.ID,"iagree").click()
        # self.driver.find_element(By.ID,"submit_btn").click()
