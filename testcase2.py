from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

#class WaitForElement(unittest.TestCase):
class TestCase2(unittest.TestCase):
      #3method test, setup and teardown are refered to as fixtures
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://travelingtony.weebly.com")
        driver.implicitly_wait(15)

    def test_AssertTitle(self):
        self.assertEqual(driver.title, "Traveling Tony's Photography - Welcome")


    def test_FindAnElement(self):
        #webElement = driver.find_element_by_xpath("//input[@name='q']")
        #webElement = driver.find_element_by_css_selector("input[name=q]")
        #webElement = driver.find_element_by_name("q")
        webElement = driver.find_element_by_class_name("wsite-search-input")
        #print webElement


    def test_FindAnElementbyxpath(self):
        webElement = driver.find_element_by_xpath("//input[@name='q']")
        #webElement = driver.find_element_by_css_selector("input[name=q]")
        #webElement = driver.find_element_by_name("q")
        #webElement = driver.find_element_by_class_name("wsite-search-input")


    def test_FindAnElementbyname(self):
        #webElement = driver.find_element_by_xpath("//input[@name='q']")
        #webElement = driver.find_element_by_css_selector("input[name=q]")
        webElement = driver.find_element_by_name("q")
        #webElement = driver.find_element_by_class_name("wsite-search-input")


    def test_FindAnElementbycss(self):
        #webElement = driver.find_element_by_xpath("//input[@name='q']")
        webElement = driver.find_element_by_css_selector("input[name=q]")
        #webElement = driver.find_element_by_name("q")
        #webElement = driver.find_element_by_class_name("wsite-search-input")


    def test_WaitForSearchField(self):
        sLocator = "input.wsite-search-input"
        sField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sLocator)))


    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
