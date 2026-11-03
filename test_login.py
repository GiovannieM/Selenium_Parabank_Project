import pytest # imports pytest framework 
from selenium import webdriver # imports webdriver core module
from selenium.webdriver.common.keys import Keys # Keys class, non-text keyboard buttons
from selenium.webdriver.common.by import By # By class, selector to locate elements
from selenium.common.exceptions import NoSuchElementException # tries to find element, used with ' try/except' block without letting test crash
from selenium.webdriver.support.ui import WebDriverWait # condition/time based wait times
from selenium.webdriver.support import expected_conditions as EC # module for checking functions on page 
from selenium.common.exceptions import TimeoutException # when condition is not met after timeframe set ( Ex. 15 secs)

from login_page import LoginPage # imports login_page py file 

# login info 
user = 'johndoe'
passwrd = '123pass'

# does not work as info is not saved as variables in login page 
# not_user = 'notjohn'
# not_passwrd = 'idkpass123'

def test_successful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login(user, passwrd)
    assert page.is_logged_in()

# defines the unsuccessful login
@pytest.mark.xfail(reason= 'Parabank demo accepts invalid credentials')
def test_unsuccessful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login('notjohn', 'idkpass123')
    assert 'Invalid login' in page.error_text()