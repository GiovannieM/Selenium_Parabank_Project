import pytest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

home_page = 'https://parabank.parasoft.com/'

# correct login info 
user = 'fastmax'
passwd = '123pass'

# incorrect login info
in_user = 'bob'
in_passwd = 'idk123'

# defines the successful login
def test_successful_login(driver):

    driver.get(home_page)
    # enters the user info 
    driver.find_element(By.NAME, 'username').send_keys(user)
    driver.find_element(By.NAME, 'password').send_keys(passwd)
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()

    wait = WebDriverWait(driver, 3)

    assert driver.find_elements(By.LINK_TEXT, 'Log Out')

# defines the unsuccessful login
@pytest.mark.xfail(reason= 'Parabank demo Site accepts invalid credentials')
def test_unsuccessful_login(driver):
    driver.get(home_page)

    # enters the incorrect user info 
    driver.find_element(By.NAME, 'username').send_keys(in_user)
    driver.find_element(By.NAME, 'password').send_keys(in_passwd)
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()

    wait = WebDriverWait(driver, 3)

    assert 'Invalid User info 'in driver.find_element(By.CLASS_NAME, 'error').text