import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service 

#  new browser for every test 
@pytest.fixture(scope='function')

# setup for chrome and all needed files to test 
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    _driver = webdriver.Chrome(options=options)
    _driver.implicitly_wait(10)
    
    # waiting for test files 
    yield _driver

    _driver.quit()

