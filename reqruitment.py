import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class TestReqruitment(unittest.TestCase): 
 def setUp(self): 
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
 
 def test_a_add_candidate(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys('Claire')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input").send_keys('Saskia')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input").send_keys('Frizt')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys('claire@gmail.com')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]').click()
    time.sleep(2)

 def test_b_search_candidate(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys('Valance')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()
    time.sleep(2)

 def test_c_reset_candidate(self): 
    driver = self.driver

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath',"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys('admin123')
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]').click()
    time.sleep(2)



 def tearDown(self): 
    self.driver.close() 
    
if __name__ == "__main__": 
 unittest.main()