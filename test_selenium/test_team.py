#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/11 8:51 下午
# @Author: chloehan
# @File  : test_team.py
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestHogwarts:

    @classmethod
    # 所有用例执行之前只初始化执行一次
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)  # 隐式等待，查找元素时给所有的findelement方法一个固定的等待时间，循环调用直到超时，默认0。5s
        self.wait = WebDriverWait(self.driver, 10)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # todo:显式等待

        element = (By.LINK_TEXT, '霍格沃兹测试学院')
        # 满足某个状态进入显式等待,找一次没找到，等0.5s再找
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_elements(element) > 1)
        # 找到了，等待过程中元素状态不对，没有定位到真正可用的元素
        self.driver.find_element(*element).click()  # *element拆箱
        # todo:隐式等待

        self.driver.find_element(By.CSS_SELECTOR, ".topic-22287 .title > a").click()

    def teardowm_method(self):
        time.sleep(20)
        self.driver.quit()
