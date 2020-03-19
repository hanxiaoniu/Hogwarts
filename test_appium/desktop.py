#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/2/29 6:54 下午
#@Author: chloehan
#@File  : desktop.py
from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http:/localhost:4723/wd/hub",caps)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
el1.click()

el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()

el3 = driver.find_element_by_id("com.xueqiu.android:id")

driver.quit()