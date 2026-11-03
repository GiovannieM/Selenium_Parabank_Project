import pytest # imports pytest framework 
from selenium import webdriver # imports webdriver core module
from selenium.webdriver.common.keys import Keys # Keys class, non-text keyboard buttons
from selenium.webdriver.common.by import By # By class, selector to locate elements
from selenium.common.exceptions import NoSuchElementException # tries to find element, used with ' try/except' block without letting test crash
from selenium.webdriver.support.ui import WebDriverWait # condition/time based wait times
from selenium.webdriver.support import expected_conditions as EC # module for checking functions on page 
from selenium.common.exceptions import TimeoutException # when condition is not met after timeframe set ( Ex. 15 secs)

from base_page import BasePage # imports BasePage 

class AccountsPage(BasePage):
    url = 'https://parabank.parasoft.com/parabank/overview.htm'

    # account_table = (By.ID, 'accountTable')
    headers = (By.CSS_SELECTOR, '#accountTable thead th')
    rows = (By.CSS_SELECTOR, '#accountTable tbody tr')
    first_account_link = (By.CSS_SELECTOR, '#accountTable  tbody tr td a')
    logout_url = (By.LINK_TEXT, 'Log Out')
    error = (By.CLASS_NAME, 'error')


    def open(self): 
        self.load_url(self.url)
        self.wait.until(EC.presence_of_element_located(self.first_account_link)) # waits for at least one account link 

    def get_headers(self):
        return [th.text for th in self.driver.find_elements(*self.headers)]

    def get_accounts(self):
        accounts = []
        for row in self.driver.find_elements(*self.rows):
            values = [td.text for td in row.find_elements(By.TAG_NAME, 'td')]   
            if values and values[0] and values[0] != 'Total':
                accounts.append(values)
        return accounts


    ####
    def is_logged_in(self, timeout=3):
        try: 
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.logout_url))
            return True
        except TimeoutException:
            return False
    
    def error_text(self):
        return self.find_element(self.error).text