from utils.ui_utils.ui_utils import UIUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Config

# Locators for the Create Account page
CREATE_ACCOUNT_URL = "https://manage.ac2.mist.com/signin.html#!signup/register"
FIRST_NAME = (By.NAME, "firstName")
LAST_NAME = (By.NAME, "lastName")
EMAIL = (By.NAME, "email")
PASSWORD = (By.NAME, "password")
CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, ".signup-form-btn")


class CreateAccountLibs:
    """
    Library class for Create Account page interactions.
    Encapsulates all UI actions on the registration form.
    """

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.ui_utils = UIUtils(driver)
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def navigate_to_create_account_page(self):
        """Navigate to the create account page and wait for form to render."""
        self.ui_utils.navigate_to(CREATE_ACCOUNT_URL)
        self.wait.until(EC.visibility_of_element_located(FIRST_NAME))

    def enter_first_name(self, name):
        """Enter first name in the registration form."""
        self.ui_utils.send_keys(*FIRST_NAME, name)

    def enter_last_name(self, name):
        """Enter last name in the registration form."""
        self.ui_utils.send_keys(*LAST_NAME, name)

    def enter_email(self, email):
        """Enter email in the registration form."""
        self.ui_utils.send_keys(*EMAIL, email)

    def enter_password(self, password):
        """Enter password in the registration form."""
        self.ui_utils.send_keys(*PASSWORD, password)

    def click_create_account(self):
        """Scroll to and click the Create Account button via JavaScript."""
        button = self.wait.until(EC.presence_of_element_located(CREATE_ACCOUNT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)