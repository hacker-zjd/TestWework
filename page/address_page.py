from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from page.add_member_page import AddMemberPage
from page.base_page import BasePage


class AddressPage(BasePage):
    _base_page = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        def wait_name(driver: WebDriver):
            ele = driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[-1]
            ele.click()
            return len(driver.find_elements(By.XPATH, '//*[@id="username"]')) > 0

        self.wait_element(wait_name)
        return AddMemberPage(self._driver)

    def delete_member(self):
        # 通过员工姓名定位到员工的父元素，然后再定位到员工对应的单选框
        # self.find(By.XPATH, f'//*[@title="{name}"]/..//input[1]').click()
        # 点击复选框选中然后点击删除按钮
        self.finds(By.XPATH, '//*[@class="qui_btn ww_btn js_delete"]')[0].click()
        locator = (By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue"]')
        # 等待自定义弹框中确定按钮完全加载后点击确认按钮
        self.wait_element(expected_conditions.element_to_be_clickable(locator))
        self.find(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue"]').click()
        # 判断词条数据是否还存在
        # TODO:实现选择多条以及全选
        return True

    def select_member_by_name(self, list_name: list):
        """
        TODO:1.通过员工名字查找员工
             2.在当前页查找不到的话翻页继续查找，如果翻到最后一页没找到返回false，找到了之后返回true

        :param list_name:
        :return:WebElement
        """
        # 通过名字查找员工
        for i in range(len(list_name)):
            self.find(By.XPATH, f'//*[@title="{list_name[i]}"]/..//input[1]').click()
        return True

    def search_member(self, kw):
        self.find(By.XPATH, '//*[@id="memberSearchInput"]').send_keys(f'{kw}')

        def wait_name(driver: WebDriver):
            return len(driver.find_elements(By.XPATH, '//*[@class="member_display_cover_detail_name"]')) > 0

        self.wait_element(wait_name)
        return len(self.finds(By.XPATH, '//*[@class="member_display_cover_detail_name"]')) > 0
