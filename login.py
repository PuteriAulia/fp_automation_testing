import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class TestLogin(unittest.TestCase): 
 def setUp(self): 
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
 
 def test_a_success_login(self): 
    driver = self.driver
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

 def test_b_failed_login_username_not_registered(self): 
    driver = self.driver
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin1')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

 def test_c_failed_login_password_not_registered(self): 
    driver = self.driver
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin1234')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

 def tearDown(self): 
    self.driver.close() 
    
if __name__ == "__main__": 
 unittest.main()