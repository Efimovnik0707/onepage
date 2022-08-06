import time
from ...utils.main.base_page import BasePage
from ...utils.assertions import MainPageAssertion


class TestMainPage:

    def test_check_title (self, browser):
        link = "https://onepage.io/"
        page = BasePage(browser)
        page.open(link)
        assertion = MainPageAssertion(browser)
        assertion.assert_should_be_main_page()