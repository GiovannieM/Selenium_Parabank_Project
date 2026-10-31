## Selenium Tests 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

## links 
home_page = 'https://parabank.parasoft.com/'
register = 'https://parabank.parasoft.com/parabank/register.htm'
overview = 'https://parabank.parasoft.com/parabank/overview.htm'

# register information
fname = 'max'
lname = 'verstopp'
address = '123 f1 way'
city = 'monaco'
state = 'nostsate'
zip_code = '12345'
phone = '123-456-7890'
ssn = '123-45-678'
user = 'fastmax'
passwd = '123pass'
confirm = passwd

# Web driver initialized 
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(home_page)

# enters the user info 
driver.find_element(By.NAME, 'username').send_keys(user)
driver.find_element(By.NAME, 'password').send_keys(passwd)
driver.find_element(By.XPATH, "//input[@value='Log In']").click()

# checks if user exist 
if driver.find_elements(By.LINK_TEXT, 'Log Out'):
    print('User Logged In...')
    print()

# check for balance 
    driver.implicitly_wait(10)
    driver.get(overview)
    account_table = driver.find_element(By.ID, 'accountTable')

    headers = account_table.find_elements(By.CSS_SELECTOR, 'thead th')
    header_values = [th.text for th in headers]
    print(header_values)

    rows = account_table.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for row in rows: 
        cells = row.find_elements(By.TAG_NAME, 'td')
        values = [td.text for td in cells]
        if values and values[0]:
            print(values)
    print()
    input("Press Enter to close the browser...")
    driver.quit()
else:
    print(' User Did Not Exist.... Registering New User')

    ## register page 
    driver.implicitly_wait(20)
    driver.get(register)

    ## entering username 
    driver.find_element(By.NAME, 'customer.firstName').send_keys(fname)
    ## entering password
    driver.find_element(By.NAME, 'customer.lastName').send_keys(lname)
    ## entering info
    driver.find_element(By.NAME, 'customer.address.street').send_keys(address)
    driver.find_element(By.NAME, 'customer.address.city').send_keys(city)
    driver.find_element(By.NAME, 'customer.address.state').send_keys(state)
    driver.find_element(By.NAME, 'customer.address.zipCode').send_keys(zip_code)
    driver.find_element(By.NAME, 'customer.phoneNumber').send_keys(phone)
    driver.find_element(By.NAME, 'customer.ssn').send_keys(ssn)
    driver.find_element(By.NAME, 'customer.username').send_keys(user)
    driver.find_element(By.NAME, 'customer.password').send_keys(passwd)
    driver.find_element(By.NAME, 'repeatedPassword').send_keys(passwd)
    ## click Register button
    driver.find_element(By.XPATH, "//input[@value='Register']").click()

    # check for balance 
    driver.implicitly_wait(10)
    driver.get(overview)
    account_table = driver.find_elements(By.ID, 'accountTable')

    headers = account_table.find_elements(By.CSS_SELECTOR, 'thead th')
    header_values = [th.text for th in headers]
    print(header_values)
    
    rows = account_table.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for row in rows: 
        cells = row.find_elements(By.TAG_NAME, 'td')
        values = [td.text for td in cells]
        if values and values[0]:
            print(values)
        print()

    input("Press Enter to close the browser...")
    driver.quit()

