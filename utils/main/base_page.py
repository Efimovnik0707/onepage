from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ...utils.auth_data import email, password
from ...utils.locators import LoginPageLocators, MainPageLocators
from selenium.webdriver.common.by import By


class BasePage (object):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)
        # accept = self.browser.find_element(*BasePageLocators.ACCEPT_BUTTON)
        # accept.click()

    def go_to_login_page(self):
        self.browser.get ("https://onepage.io/")
        self.browser.find_element(*MainPageLocators.LOGIN_BTN)
        
    def login(self, email: str = email, password: str = password):
        self.browser.get ("https://onepage.io/auth/login")
        
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys (email)
        password_input = self.browser.find_element (*LoginPageLocators.PASSWORD)
        password_input.send_keys (password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        
        wait = WebDriverWait(self.browser, 1).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button:nth-child(3)")))
        # new_page = WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Create site')]")))
        

    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
         WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, how, what, timeout=15):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
