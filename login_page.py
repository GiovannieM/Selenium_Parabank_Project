import pytest # imports pytest framework 
from selenium import webdriver # imports webdriver core module
from selenium.webdriver.common.keys import Keys # Keys class, non-text keyboard buttons
from selenium.webdriver.common.by import By # By class, selector to locate elements
from selenium.common.exceptions import NoSuchElementException # tries to find element, used with ' try/except' block without letting test crash
from selenium.webdriver.support.ui import WebDriverWait # condition/time based wait times
from selenium.webdriver.support import expected_conditions as EC # module for checking functions on page 
from selenium.common.exceptions import TimeoutException # when condition is not met after timeframe set ( Ex. 15 secs)

from base_page import BasePage # imports BasePage 

class LoginPage(BasePage):
    url = 'https://parabank.parasoft.com/'

    user = (By.NAME, 'username')
    passwrd = (By.NAME, 'password')
    login_button = (By.XPATH, "//input[@value='Log In']")
    logout_url = (By.LINK_TEXT, 'Log Out')
    error = (By.CLASS_NAME, 'error')

    def open(self): 
        self.load_url(self.url)

    def login(self, user, passwrd):
        self.enter_text(self.user, user)
        self.enter_text(self.passwrd, passwrd)
        self.click_element(self.login_button)

    def is_logged_in(self, timeout=3):
        try: 
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.logout_url))
            return True
        except TimeoutException:
            return False
    
    def error_text(self):
        return self.find_element(self.error).text
