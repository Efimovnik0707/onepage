import time

import pytest
import allure

from ...utils.locators import LoginPageLocators

from ...utils.assertions import ProjectPageAssertion
from ...utils.main.base_page import BasePage
from ...pages.projectpage import ProjectPage


class TestProjects:
    # @pytest.mark.skip
    @pytest.mark.regress
    @pytest.mark.functional
    @pytest.mark.smoke
    @allure.description("Verify that user can create project")
    def test_create_new_project(self, browser):
        """
        STR:
        1. Open main page
        2. Click on login button
        3. Input correct value in fields
        4. Click "Login"
        5. Click "Create Project"
        6. Input name of new project
        7. Click "Create Project"
        8. Click "Publish"
        9. Verify that success message presented
        """
        link = "https://onepage.io/"
        page = BasePage(browser)
        page.open(link)
        page.login()
        project_page = ProjectPage(browser)
        project_page.create_new_project(project_name="mynewproject")

    # @pytest.mark.skip
    @pytest.mark.functional
    @allure.description("Verify that user can delete project")
    def test_delete_project(self, browser):
        """
        STR:
        1. Open main page
        2. Click on login button
        3. Input correct value in fields
        4. Click "Login"
        5. Click "Create Project"
        6. Input name of new project
        7. Click "Create Project"
        8. Click "Publish"
        9. Verify that success message presented
        """
        link = "https://onepage.io/"
        page = BasePage(browser)
        page.open(link)
        page.login()
        time.sleep(5)
        project_page = ProjectPage(browser)
        project_page.delete_project(project_name="mynewproject", exist=0)
