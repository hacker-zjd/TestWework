from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.add_member_page import AddMemberPage
from page.base_page import BasePage


class AddressPage(BasePage):
    _base_page = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        def wait_name(driver: WebDriver):
            ele = driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')
            ele[-1].click()
            return len(driver.find_elements(By.XPATH, '//*[@id="username"]')) > 0

        self.wait_element(wait_name)
        return AddMemberPage(self._driver)

    def delete_member_by_name(self, name):
        self.find(By.XPATH, f'//*[@title="{name}"]/..//input[1]').click()
        self.find(By.XPATH, '//*[@class="qui_btn ww_btn js_delete"]')[0].click()
        alert = self._driver.switch_to_alert()
        alert.accept()
        return len(self.finds(By.XPATH, f'//*[@title="{name}"]')) <= 0
