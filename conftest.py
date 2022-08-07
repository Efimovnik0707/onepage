import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from .utils.auth_data import email, password
from .utils.locators import LoginPageLocators
from .utils.locators import ProjectsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="function")
def browser():

    print("\nstart browser chrome for test...")
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver
    print("\nquit browser...")
    driver.quit()


@pytest.fixture(scope="function")
def login():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    try:
        # driver.get ("https://onepage.io/auth/login")

        # email_input = driver.find_element(*LoginPageLocators.EMAIL)
        # email_input.send_keys (email)
        # password_input = driver.find_element (*LoginPageLocators.PASSWORD)
        # password_input.send_keys (password)
        # login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # wait = WebDriverWait(driver, 1).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button:nth-child(3)")))

        # new_page = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Create site')]")))

        # #cookies
        # # cookies = driver.get_cookies()
        # # print (cookies)
        # pickle.dump(driver.get_cookies(), open(f'tomatik0707_cookies.pkl', "wb"))

        driver.get("https://onepage.io/auth/login")
        driver.delete_all_cookies()
        for cookie in pickle.load(open(f"tomatik0707_cookies.pkl", "rb")):
            cookie["domain"] = ".onepage.io"
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(e)

    except Exception as ex:
        print(ex)
    finally:
        yield driver
        print("\nquit browser...")
        driver.quit()
