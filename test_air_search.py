import pytest
from .pages.base_page import base_url
from .pages.air_search import AirSearch
from .pages.login import Login


@pytest.mark.parametrize('local', [".com", pytest.param(".co.uk", marks=pytest.mark.skip(
    reason="Just for example")), ".ae"])
class TestSearch:

    @pytest.fixture(scope="function")
    def link(self, local):
        return f"{base_url}{local}"

    @pytest.mark.smoke
    def test_search_for_unauth_user(self, browser, link):
        search = AirSearch(browser, link)
        login = Login(browser, link)

        search.open()
        search.air_search()
        login.incorrect_login()
