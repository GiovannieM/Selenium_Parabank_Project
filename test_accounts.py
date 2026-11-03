import pytest # imports pytest framework 
from selenium import webdriver # imports webdriver core module
from selenium.webdriver.common.keys import Keys # Keys class, non-text keyboard buttons
from selenium.webdriver.common.by import By # By class, selector to locate elements
from selenium.common.exceptions import NoSuchElementException # tries to find element, used with ' try/except' block without letting test crash
from selenium.webdriver.support.ui import WebDriverWait # condition/time based wait times
from selenium.webdriver.support import expected_conditions as EC # module for checking functions on page 
from selenium.common.exceptions import TimeoutException # when condition is not met after timeframe set ( Ex. 15 secs)

from login_page import LoginPage
from accounts_page import AccountsPage # imports accounts_page py file 

user = 'johndoe'
passwrd = 'notpassword123'

def test_accounts_table_has_rows(driver):
    login = LoginPage(driver)
    login.open() 
    login.login(user, passwrd)
    assert login.is_logged_in()   

    accounts = AccountsPage(driver)
    accounts.open()
    rows = accounts.get_accounts()
    assert len(rows) > 0 
