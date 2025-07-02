import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test.dataveg import dataveg
#import test.locators
from test.utils import frequrntFunctions


#import dataveg
#from test.conftest import invokeDriver

class Test_VegCart():
    def test_vegcart(self, invokeDriver):
        vegNameList = []
        CartList = []
        driver=invokeDriver
        driver.get(dataveg["url1"])
        #wait=WebDriverWait(driver)
        #wait.until(expected_conditions.visibility_of_element_located())
        time.sleep(6)
        ff=frequrntFunctions(driver)
        ff.sendKeys("search","ber")
        time.sleep(5)
        #vegNames=driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
        listOfVegNames=frequrntFunctions.findElementsByXpath(driver,dataveg["vegNames"])
        for vegName in listOfVegNames:
            vegNameList.append(vegName.text)
            assert "ber" in vegName.text,"search word not present in veglist"
        lists=driver.find_elements(By.XPATH,"//div[@class='products']//div[@class='product-action']/button")
        for list in lists:
            list.click()
        driver.find_element(By.XPATH,"//a[@class='cart-icon']/img").click()
        driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
        time.sleep(4)
        listInCart=driver.find_elements(By.XPATH,"//p[@class='product-name']")
        for items in listInCart:
            CartList.append(items.text)
        print(CartList,vegNameList)
        assert vegNameList==CartList, "items added is not matching with items in cart"
        prices= driver.find_elements(By.XPATH,"//tr/td[5]/p[@class='amount']")
        amount=0
        for price in prices:
            amount=amount+int(price.text)
        totalCost=driver.find_element(By.XPATH,"//span[@class='totAmt']")
        assert amount==int(totalCost.text), "total value calculated is not matching with prices in cart"
        driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("abv")
        driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
        wait=WebDriverWait(driver,15)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
        print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)
        driver.find_element(By.XPATH,"//input[@class='promoCode']").clear()
        driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
        driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
        time.sleep(7)
        promoCode=driver.find_element(By.XPATH,"//span[@class='promoInfo']").text
        print(promoCode)
        if promoCode=="Code applied ..!":
            promotext=driver.find_element(By.XPATH,"//input[@class='promoCode']").get_attribute("value")
            print(promotext)
        afterDiscount=driver.find_element(By.XPATH,"//span[@class='discountAmt']").text
        assert float(afterDiscount)<float(totalCost.text)
        time.sleep(2)