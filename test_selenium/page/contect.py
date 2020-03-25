#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/24 11:13 下午
# @Author: chloehan
# @File  : contect.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Contect:

    _add_member_button=(By.CSS,"XXXX")
    def add_member(self,data):
        self.driver.find_element("添加成员").click()
        # sendkeys
        # click save
        return self
    def add_member_error(self,data):
        return AddMemberPage()

    def search(self):
        pass

    def import_users(self):
        pass

    def export_users(self):
        pass

    def set_department(self):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass
