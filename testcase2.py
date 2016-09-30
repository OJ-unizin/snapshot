from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import unittest
import time

##Find and validate all elements on the Login page.

#class WaitForElement(unittest.TestCase):
class TestCase2(unittest.TestCase):
      #3method test, setup and teardown are refered to as fixtures
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://unizin.instructure.com/courses/151/external_tools/207")
        #driver.implicitly_wait(15)

    def test_AssertTitle(self):
        self.assertEqual(driver.title, "Log In to Canvas")


    def test_FindAnElement(self):
        email_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pseudonym_session_unique_id"))
        email_Element.clear()
        email_Element.send_keys("oscar.juarez@unizin.org")


    #def test_FindAnElementbyxpath(self):
        password_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pseudonym_session_password"))
        password_Element.clear()
        password_Element.send_keys("unizin001")

        #LogIn_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[contains(.,'Log In')]"))
        #LogIn_Element.click()
        password_Element.send_keys(Keys.RETURN)
        print driver.title


        webElement = WebDriverWait(driver, 20).until(lambda driver:driver.find_element_by_xpath("//a[contains(.,'Snapshot')]"))
        webElement.click()

    #def test_1(self):
        #iframe = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pseudonym_session_password"))
        #driver.switch_to_frame('instructure_ajax_error_result')
        print driver.title

        time.sleep(20)

        ##driver.switch_to_default_content()

        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        #browser.get_screenshot_as_file('screenshot-%s.png' % now)
        driver.save_screenshot('screenshot-%s.jpg' % now)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
