import pytest

from page.address_page import AddressPage
from page.main_page import MainPage
from until.yaml_until import YamlUntil


def get_data():
    yaml_until = YamlUntil()
    return yaml_until.get_data()['info']


@pytest.fixture(params=get_data())
def search_data(request):
    return request.param


class TestMember:

    def setup(self):
        self.main = MainPage()
        self.address = AddressPage()

    @pytest.mark.skip
    @pytest.mark.parametrize('username, member_id, member_phone', get_data())
    def test_add(self, username, member_id, member_phone):
        self.address.goto_add_member().add_member(username, member_id, member_phone)

    def test_search(self, search_data):
        a = self.address.search_member(search_data[0])
        print(search_data[0])
        assert a

    @pytest.mark.skip
    def test_del(self):
        assert self.address.delete_member_by_name('lucky_boy2')
