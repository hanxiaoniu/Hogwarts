#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/25 10:34 下午
# @Author: chloehan
# @File  : register.py
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self, compname, mgrname):
        self.driver.find_element(By.ID, "corp_name").send_keys(compname)
        self.driver.find_element(By.ID, "manager_name").send_keys(mgrname)
        self.driver.find_element(By.ID, "iagree").click()
        self.driver.find_element(By.ID, "submit_btn").click()
