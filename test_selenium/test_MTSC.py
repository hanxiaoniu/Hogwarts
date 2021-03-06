#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/14 9:40 下午
# @Author: chloehan
# @File  : test_MTSC.py
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestMTSC:
    def setup_method(self):
        # 多浏览器
        browser = os.getenv("browser").lower()
        if browser == "headless":
            self.driver = webdriver.PhantomJS()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            # options
            self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com')
        self.driver.implicitly_wait(5)

    def test_page(self):
        self.driver.find_element(By.CSS_SELECTOR, '[title="MTSC2020 中国互联网测试开发大会议题征集"]').click()
        element = (By.CSS_SELECTO, '.toc-container.dropdown')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.CSS_SELECTOR, '.toc-item:nth-child(4) > .toc-item-link').click()

    def test_submit(self):
        self.driver.get('https://testerhome.com/topics/21044')
        submit = (By.CSS_SELECTOR, '#reply-button')
        # self.wait(10,expected_conditions.element_to_be_clickable(submit))
        # self.driver.switch_to.frame(0)
        self.driver.find_element(*submit).click()

    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.find_element(By.LINK_TEXT, '第六届中国互联网测试开发大会').click()
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.LINK_TEXT, '演讲申请').click()

    def test_js(self):
        # json当前网页的打开时间
        for code in ["return document.title",
                     'return document.querySelector(".active").className',
                     'JSON.stringify(performance.timing)'
                     ]:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        time.sleep(10)
        self.driver.quit()
