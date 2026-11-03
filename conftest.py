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


import os

@pytest.hookimpl(hookwrapper=True) # lets pytest create the first result
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed: # only looks at test itself 
        driver = item.funcargs.get("driver") # grabs browser test was using
        if driver:
            os.makedirs("screenshots", exist_ok=True) # creates screenshot folder
            driver.save_screenshot(f"screenshots/{item.name}.png") # saves png named after test