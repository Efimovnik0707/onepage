from ..utils.locators import MainPageLocators
from ..utils.main.base_page import BasePage

class LoginPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click
        