# coding=utf-8
# @Author:hacker-zjd
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    1.初始化webdriver
    2.封装定位方法
    3.封装隐式等待方法以便调用
    """
    _driver = None
    _base_page = ""

    def __init__(self, driver: WebDriver = None):
        """
        :param driver: browser webdriver
        :type driver:webdriver
        """
        if self._driver is None:
            options = Options()
            """
            复用已存在的浏览器，需要先执行命令: 
            chrome --romote-debugging-port=127.0.0.1:9993
            """
            options.debugger_address = "127.0.0.1:9993"
            self._driver = webdriver.Chrome(
                executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe", options=options)
        else:
            self._driver = driver
        self._driver.implicitly_wait(15)
        if self._base_page != "":
            self._driver.get(self._base_page)

    def find(self, by, locator):
        """
        :param by:定位方法
        :param locator:定位器
        :return:element 元素
        """
        return self._driver.find_element(by, locator)

    def finds(self, by, locator) -> List[WebElement]:
        """
        :param by:定位方法
        :param locator:定位器
        :return:element 元素
        :rtype: list of WebElement
        """
        return self._driver.find_elements(by, locator)

    def wait_element(self, method, time=10):
        """
        封装元素可点击的显式等待方法以便调用
        :param method: 方法名
        :param time: 等待时间
        :return:
        """
        return WebDriverWait(self._driver, time).until(method)
