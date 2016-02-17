#! /usr/bin/env python
# --*--coding:utf-8 --*--

import os
from selenium import webdriver
import unittest


class Example(unittest.TestCase):

    def setUp(self):
        self.chromedriver = "../driver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = self.chromedriver

    def test_chrome(self):
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")

    def test_ie(self):
        self.driver = webdriver.Ie(r"../driver/IEDriverServer.exe")
        self.driver.maximize_window()
        self.driver.get("http://www.google.com.hk")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()