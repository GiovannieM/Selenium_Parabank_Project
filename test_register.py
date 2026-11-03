import pytest # imports pytest framework 
from selenium import webdriver # imports webdriver core module
from selenium.webdriver.common.keys import Keys # Keys class, non-text keyboard buttons
from selenium.webdriver.common.by import By # By class, selector to locate elements
from selenium.common.exceptions import NoSuchElementException # tries to find element, used with ' try/except' block without letting test crash
from selenium.webdriver.support.ui import WebDriverWait # condition/time based wait times
from selenium.webdriver.support import expected_conditions as EC # module for checking functions on page 
from selenium.common.exceptions import TimeoutException # when condition is not met after timeframe set ( Ex. 15 secs)

import time
from register_page import RegisterPage # imports login_page py file 

fname = 'john'
lname = 'doe'
address = '123 way'
city = 'dallas'
state = 'texas'
zip_code = '12345'
phone = '123-456-7890'
ssn = '123-45-678'
user = 'userjohn'
passwrd = '123pass'
confirm = passwrd

def test_successful_register(driver):
    user = f'user_{int(time.time())}' # creates neww user based on time
    page = RegisterPage(driver)
    page.open()
    page.register(fname, lname, address, city, state, zip_code, 
                  phone, ssn, user, passwrd)

    assert page.is_logged_in()

def test_register_duplicate_username(driver):
    user = f'user_{int(time.time())}' # creates neww user based on time
    page = RegisterPage(driver)

    # first time new user 
    page.open()
    page.register(fname, lname, address, city, state, zip_code, 
                  phone, ssn, user, passwrd) 
    page.driver.delete_all_cookies()  # log out and clears the session (cookies)

    # duplicate users
    page.open()
    page.register(fname, lname, address, city, state, zip_code, 
                  phone, ssn, user, passwrd)
    assert 'already exists' in page.error_text()

