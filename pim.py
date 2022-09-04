import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class TestReqruitment(unittest.TestCase): 
 def setUp(self): 
    self.driver = webdriver.Chrome(ChromeDriverManager().install())

 
 def test_a_add_employee(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys('Anita')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input").send_keys('Saraswati')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys('Fahma')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
    time.sleep(2)

 def test_b_search_by_name_employee(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys('Odis  Adalwin')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(2)


 def test_c_reset_employee(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()
    time.sleep(2)
 

 def tearDown(self): 
    self.driver.close() 
    
if __name__ == "__main__": 
 unittest.main()