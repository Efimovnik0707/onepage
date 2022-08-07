from ..utils.main.base_page import BasePage
from ..utils.locators import ProjectsPageLocators
from ..utils.assertions import ProjectPageAssertion

from typing import AnyStr, Dict, Any, Union, List, Literal
import time

import pdb


class ProjectPage(BasePage):
    def create_new_project(self, project_name: str):
        ProjectPageAssertion.assert_project_exist(
            self, project_name=project_name, exist=0
        )
        # ProjectPageAssertion.assert_before_create(self, project_name=project_name)
        create_btn = self.browser.find_element(*ProjectsPageLocators.CREATE_BTN).click()
        create_page = self.browser.find_element(
            *ProjectsPageLocators.BLANK_PAGE_BTN
        ).click()
        title = self.browser.find_element(*ProjectsPageLocators.TITLE)
        title.send_keys(f"{project_name}")
        new_create_btn = self.browser.find_element(
            *ProjectsPageLocators.NEW_CREATE_BTN
        ).click()
        publish_brn = self.browser.find_element(*ProjectsPageLocators.PUBLISH).click()
        ProjectPageAssertion.assert_should_success_message(self)

    def delete_project(self, project_name: str, exist: Union[bool, int] = 0):
        ProjectPageAssertion.assert_project_exist(
            self, project_name=project_name, exist=1
        )
        # ProjectPageAssertion.assert_before_delete(
        #     self, project_name=project_name, exist=exist
        # )
        dots_btn = self.browser.find_element(*ProjectsPageLocators.DOTS_BTN).click()
        archive_btn = self.browser.find_element(
            *ProjectsPageLocators.ARCHIVE_BTN
        ).click()
        archive_popup_btn = self.browser.find_element(
            *ProjectsPageLocators.ARCHIVE_POPUP_BTN
        ).click()

        archive_menu_btn = self.browser.find_element(
            *ProjectsPageLocators.ARCHIVE_MENU_BTN
        ).click()
        time.sleep(1)

        dots_btn = self.browser.find_element(*ProjectsPageLocators.DOTS_BTN).click()
        delete_btn = self.browser.find_element(*ProjectsPageLocators.DELETE_BTN).click()
        delete_popup_btn = self.browser.find_element(
            *ProjectsPageLocators.DELETE_POPUP_BTN
        ).click()
        time.sleep(1)
        active_menu_btn = self.browser.find_element(
            *ProjectsPageLocators.ACTIVE_MENU_BTN
        ).click()
        time.sleep(1)
        ProjectPageAssertion.assert_project_exist(
            self, project_name=project_name, exist=0
        )
        # ProjectPageAssertion.assert_project_delete(self, project_name=project_name)
