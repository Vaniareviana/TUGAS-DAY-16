import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_failed_login(self): #test case 1
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        driver.find_element(By.ID,"password").send_keys("") 
        driver.find_element(By.NAME, "login-button").click() 
        respon = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", respon)  

    def test_success_login(self): #test case 2
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()

    def test_success_sauce_labs(self): #test case 3
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
   
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()