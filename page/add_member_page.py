from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self, username, member_id, member_phone):
        self.find(By.XPATH, '//*[@id="username"]').send_keys(f'{username}')
        self.find(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(f'{member_id}')
        self.find(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(f'{member_phone}')
        self.find(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]').click()
        ele = self.finds(By.XPATH, '//*[@class="js_mod_party_name"]')
        return len(ele) > 0
