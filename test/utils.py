from selenium.webdriver.common.by import By

import test.locators
#from practice.vegcart import driver
from test import locators


class frequrntFunctions():
    def __init__(self,driver):
        self.driver=driver

    def sendKeys(self,attribute,text):
        self.driver.find_element(*getattr(locators, attribute)).send_keys(text)

    def findElementsByXpath(driver,locator):
        listOfElements=driver.find_elements(By.XPATH,locator)
        return listOfElements