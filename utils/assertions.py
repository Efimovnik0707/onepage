from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.locators import LoginPageLocators
from ..utils.locators import ProjectsPageLocators
from ..utils.locators import MainPageLocators
from ..utils.main.base_page import BasePage
from typing import AnyStr, Dict, Any, Union, List, Literal


class MainPageAssertion(BasePage):
    def assert_should_be_main_page(self):
        assert self.is_element_present(*MainPageLocators.TITLE), "Title was not found"
        link = "https://onepage.io/"
        assert link == self.browser.current_url, "'onepage.io' not current url"


class LoginPageAssertion(BasePage):
    def assert_should_login(self):
        assert self.is_element_present(
            *ProjectsPageLocators.AVATAR_ICON
        ), "Login has not been implemented"

    def assert_should_be_error_message(self, excepted_message: str):
        error_message = self.browser.find_element(*LoginPageLocators.ERROR_MSG).text
        assert error_message == excepted_message, "Error message was not find"


class ProjectPageAssertion(BasePage):
    def assert_should_success_message(self):
        assert self.is_element_present(
            *ProjectsPageLocators.SUCCESS_MESSAGE
        ), "Project was not created"

    def assert_project_exist(
        self, project_name: str, exist: Union[bool, int] = 0
    ) -> None:
        title = self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME).text
        found = 0 if exist else 1
        if project_name == title:
            found = 1
        else:
            found = 0
            assert not found, f"Project with name {project_name} not found"
        if not exist:
            assert not found, f"Project with name {project_name} not found"
