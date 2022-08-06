import time

import pytest

from ...utils.locators import LoginPageLocators

from ...utils.assertions import LoginPageAssertion
from ...utils.main.base_page import BasePage


class TestLogin():

    
    def test_should_be_login(self, browser):
        link = "https://onepage.io/"
        page = BasePage(browser)
        page.open(link)
        page.login()
        time.sleep(3)

    @pytest.mark.parametrize('email', ['test123', 'test @gmail.com', '<script>'])
    def test_negative_email(self, browser, email):
        excepted_message = "Invalid E-mail"
        link = "https://onepage.io/"
        page = BasePage(browser)
        page.open(link)
        page.login(email=email)
        assertion = LoginPageAssertion(browser)
        assertion.assert_should_be_error_message(excepted_message=excepted_message)
        
