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

        #Courses link
        ##Courseslink_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[@href='/courses']"))
        Courseslink_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[@id='global_nav_courses_link']"))
        print Courseslink_Element.text
        Courseslink_Element.click()
        time.sleep(2)

        #All Courses link
        #AllCourseslink_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//span[@class='name']"))
        #AllCourseslink_Element.click()

        #[CMP Production] Template Course link
        cmpProductionCourse_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//span[@class='name']"))
        print cmpProductionCourse_Element.text
        cmpProductionCourse_Element.click()
        time.sleep(2)

        #Snapshot menu link
        webElement_Snapshot = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(.,'Snapshot')]"))
        print webElement_Snapshot.text
        webElement_Snapshot.click()
        time.sleep(5)


        #print driver.title

####    #Show / Hide Course menu
        #webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@aria-hidden='true']"))
        #webElement = WebDriverWait(driver, 10).unitil(lambda driver: driver.find_element_by_xpath("//button[@aria-label='Hide courses menu']"))
        webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@id='courseMenuToggle']"))
        webElement.click()
        time.sleep(5)
        webElement.click()
        time.sleep(5)

        #Validate EAP link
        #webElement_EAP102 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//span[contains(.,'EAP 102')]"))
        webElement_EAP102 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('EAP 102'))
        print webElement_EAP102.text
        webElement_EAP102.click()
        time.sleep(5)

        webElementss = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(.,'Snapshot')]"))
        print webElementss.text
        webElementss.click()
        time.sleep(5)

        #Validate "[CMP Production] Template Course exist"
        webElement_2 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//span[contains(.,'[CMP Production] Template Course')]"))
        #webElement_2 = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('[CMP Production] Template Course'))
        print webElement_2.text
        webElement_2.click()
        time.sleep(5)

        webElement1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(.,'Snapshot')]"))
        print webElement1.text
        webElement1.click()
        time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
