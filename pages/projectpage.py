from ..utils.main.base_page import BasePage
from ..utils.locators import ProjectsPageLocators
import time


class ProjectPage(BasePage):
    def create_new_project(self, project_name: str):
        create_btn = self.browser.find_element(*ProjectsPageLocators.CREATE_BTN).click()
        create_page = self.browser.find_element(*ProjectsPageLocators.BLANK_PAGE_BTN).click()
        title = self.browser.find_element(*ProjectsPageLocators.TITLE)
        title.send_keys (f'{project_name}')
        new_create_btn = self.browser.find_element(*ProjectsPageLocators.NEW_CREATE_BTN).click()
        publish_brn = self.browser.find_element(*ProjectsPageLocators.PUBLISH).click()

    def delete_project(self, project_name: str):
        dots_btn = self.browser.find_element(*ProjectsPageLocators.DOTS_BTN).click()
        archive_btn = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_BTN).click()
        archive_popup_btn = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_POPUP_BTN).click()
        archive_menu_btn = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_MENU_BTN).click()
        time.sleep(1)
        dots_btn = self.browser.find_element(*ProjectsPageLocators.DOTS_BTN).click()
        delete_btn = self.browser.find_element(*ProjectsPageLocators.DELETE_BTN).click()
        delete_popup_btn = self.browser.find_element(*ProjectsPageLocators.DELETE_POPUP_BTN).click()
        time.sleep(1)
        
        
        
            
            