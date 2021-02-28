from page.address_page import AddressPage
from page.main_page import MainPage


class TestMember:

    def setup(self):
        self.main = MainPage()
        self.address = AddressPage()

    def test_add(self):
        self.main.goto_address().add_member()
        self.address.goto_add_member().add_member()