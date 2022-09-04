import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class TestReqruitment(unittest.TestCase): 
 def setUp(self): 
    self.driver = webdriver.Chrome(ChromeDriverManager().install())

 
 def test_a_edit_middle_name_profil(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys('Star')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
    time.sleep(2)

 def test_b_edit_city_profil(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/contactDetails/empNumber/7")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys('New York')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
    time.sleep(2)


 def tearDown(self): 
    self.driver.close() 
    
if __name__ == "__main__": 
 unittest.main()