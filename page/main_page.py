from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.add_member_page import AddMemberPage
from page.address_page import AddressPage
from page.base_page import BasePage


class MainPage(BasePage):
    _base_page = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_address(self):
        # click add_member of main page
        self.find(By.XPATH, '//*[@id="menu_contacts"]').click()
        return AddressPage(self._driver)
