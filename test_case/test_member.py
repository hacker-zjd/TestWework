import pytest

from page.address_page import AddressPage
from page.main_page import MainPage


class TestMember:

    def setup(self):
        self.main = MainPage()
        self.address = AddressPage()

    @pytest.mark.skip
    def test_add(self):
        # self.main.goto_address().add_member()
        assert self.address.goto_add_member().add_member()

    def test_del(self):
        assert self.address.delete_member_by_name('lucky_boy5')
