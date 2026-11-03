import pytest # imports pytest framework 
from selenium import webdriver # imports webdriver core module
from selenium.webdriver.common.keys import Keys # Keys class, non-text keyboard buttons
from selenium.webdriver.common.by import By # By class, selector to locate elements
from selenium.common.exceptions import NoSuchElementException # tries to find element, used with ' try/except' block without letting test crash
from selenium.webdriver.support.ui import WebDriverWait # condition/time based wait times
from selenium.webdriver.support import expected_conditions as EC # module for checking functions on page 
from selenium.common.exceptions import TimeoutException # when condition is not met after timeframe set ( Ex. 15 secs)

from base_page import BasePage # imports BasePage 

class RegisterPage(BasePage): # gets all registration elements 
    url = 'https://parabank.parasoft.com/parabank/register.htm'
    
    fname = (By.NAME, 'customer.firstName')
    lname = (By.NAME, 'customer.lastName')
    address = (By.NAME, 'customer.address.street')
    city = (By.NAME, 'customer.address.city')
    state = (By.NAME, 'customer.address.state')
    zip_code = (By.NAME, 'customer.address.zipCode')
    phone = (By.NAME, 'customer.phoneNumber')
    ssn = (By.NAME, 'customer.ssn')
    user = (By.NAME, 'customer.username')
    passwd = (By.NAME, 'customer.password')
    confirm = (By.NAME, 'repeatedPassword')
    ## click Register button
    register_button = (By.XPATH, "//input[@value='Register']")
    logout_url = (By.LINK_TEXT, 'Log Out') 
    error = (By.CLASS_NAME, 'error')

    def open(self): # opens url page
        self.load_url(self.url)

    def register(self, fname, lname, address, city, state, zip_code, phone, ssn, user, passwrd): # fills out form elements
        self.enter_text(self.fname, fname)
        self.enter_text(self.lname, lname)
        self.enter_text(self.address, address)
        self.enter_text(self.city, city)
        self.enter_text(self.state, state)
        self.enter_text(self.zip_code, zip_code)
        self.enter_text(self.phone, phone)
        self.enter_text(self.ssn, ssn)
        self.enter_text(self.user, user)
        self.enter_text(self.passwd, passwrd)
        self.enter_text(self.confirm, passwrd)
        self.click_element(self.register_button) 


    def is_logged_in(self, timeout=3): # waits 3 seconds for 'log out' link to appear 
        try: 
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.logout_url))
            return True
        except TimeoutException:
            return False


    def error_text(self): # finds error message on page and displays as text 
        return self.find_element(self.error).text