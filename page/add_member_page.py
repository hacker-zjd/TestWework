from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self):
        self.find(By.XPATH, '//*[@id="username"]').send_keys('lucky_boy3')
        self.find(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys('my_lucky3')
        self.find(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys('13354681990')
        self.find(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]').click()
        sleep(1)
        return True
