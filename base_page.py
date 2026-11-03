from selenium.webdriver.support.ui import WebDriverWait # condition/time based wait times
from selenium.webdriver.support import expected_conditions as EC # module for checking functions on page 

class BasePage: # class name
    def __init__(self, driver): # auto runs when new instance is created and takes 'driver' as argument
        self.driver = driver # ensures every instance had a active window
        self.wait = WebDriverWait(driver, 15) # driver waits for 15 seconds 

    def load_url(self, url): # takes 'url' variable as argument
        self.driver.get(url)

    def find_element(self, locator): # takes 'locator' as argument, locates web element
        return self.wait.until(EC.presence_of_element_located(locator)) # explicit wait until element is found on page

    def click_element(self, locator): # method to interact (click) elements on page
        self.wait.until(EC.element_to_be_clickable(locator)).click() # waits 15s for element to be visable and enalbled to be clicked, when ready it is clicked 

    def enter_text(self, locator, text): # method to type into fields, requires locator & text
        element = self.find_element(locator) # finding and locate text box and saves as variable 'element'
        element.clear() # clears pre-existing text box
        element.send_keys(text) #keyboard stroke to type text 

    def get_page_title(self): # method to get window text title
        return self.driver.title  # reads current title