from sre_constants import SUCCESS
from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, "input[type=email]")
    PASSWORD = (By.CSS_SELECTOR, "input[type=password]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button:nth-child(3)")
    ERROR_MSG = (By.XPATH, "//*[contains(text(), 'Invalid E-mail')]")
    ERROR_MSG2 = (By.XPATH, "//*[contains(text(), 'login.http_errors.undefined')]")


class ProjectsPageLocators:
    CREATE_BTN = (By.XPATH, "//*[contains(text(), 'Create site')]")
    AVATAR_ICON = (By.CSS_SELECTOR, "div.one-builder-avatar.one-ui-view")
    BLANK_PAGE_BTN = (By.XPATH, "//*[contains(text(), 'Create a page')]")
    TITLE = (By.CSS_SELECTOR, "input[name=project_title]")
    PROJECT_NAME = (By.CSS_SELECTOR, ".one-ui-title[data-margin='sm']")
    PUBLISH = (By.XPATH, "//*[contains(text(), 'Publish')]")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Successfully published')]")
    NEW_CREATE_BTN = (
        By.CSS_SELECTOR,
        "button[data-loading='false'] span[class='one-ui-button__content']",
    )

    DOTS_BTN = (
        By.CSS_SELECTOR,
        "button[data-size='sm'] span[class='one-ui-button__content']",
    )
    ARCHIVE_BTN = (
        By.CSS_SELECTOR,
        "body > div:nth-child(19) > div.one-ui-popout__menu.one-ui-view > div > div > div > div > div > div > button:nth-child(5)",
    )
    ARCHIVE_POPUP_BTN = (
        By.CSS_SELECTOR,
        "button[data-type='alert'] span[class='one-ui-button__content']",
    )

    ARCHIVE_MENU_BTN = (
        By.CSS_SELECTOR,
        "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(5)",
    )

    DELETE_BTN = (
        By.CSS_SELECTOR,
        "div[class='one-ui-popout__menu one-ui-view'] div:nth-child(1) div:nth-child(1) div:nth-child(1) button:nth-child(2) span:nth-child(1)",
    )
    DELETE_POPUP_BTN = (
        By.CSS_SELECTOR,
        "button[data-type='alert'] span[class='one-ui-button__content']",
    )

    ACTIVE_MENU_BTN = (
        By.CSS_SELECTOR,
        "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)",
    )
    PROJECT_NAME = (By.CSS_SELECTOR, ".one-ui-title[data-margin='sm']")
    PROJECT_BLOCK = (By.CSS_SELECTOR, "div.page-card.one-ui-view")


class MainPageLocators:
    LOGIN_BTN = (By.XPATH, "//*[contains(text(), 'Login')]")
    REG_BTN = (By.XPATH, "//*[contains(text(), 'Sign up')]")
    FREE_PLAN = (By.XPATH, "//*[contains(text(), 'Start for free')]")
    TITLE = (By.XPATH, "//*[contains(text(), 'The website-building tool you’ll')]")


class RegistrationPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[name=fname]")
    LAST_NAME = (By.CSS_SELECTOR, "input[name=lname]")
    EMAIL = (By.CSS_SELECTOR, "input[name=email]")
    PASSWORD = (By.CSS_SELECTOR, "input[name=password]")
    TERMS = (By.CSS_SELECTOR, "div:nth-child(4) > div > div > input[type=checkbox]")
    CREATE_BTN = (By.XPATH, "//*[contains(text(), 'Create my Onepage Account')] ")
