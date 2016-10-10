from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time

##Find and validate all elements on the Login page.

#class WaitForElement(unittest.TestCase):
class TestCase1(unittest.TestCase):
      #3method test, setup and teardown are refered to as fixtures
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://unizin.instructure.com/courses/151/external_tools/207")
        #driver.implicitly_wait(15)

    def test_AssertTitle(self):
        #Validate that the page tiltle is correct
        self.assertEqual(driver.title, "Log In to Canvas")
        time.sleep(5)

    def test_assertText_Email(self):
        #Validate that the "Email" label is present.
        test_assertText_Email = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//label[@for='pseudonym_session_unique_id']"))
        #print webElement.text
        assert test_assertText_Email.text == 'Email'
        print 'test_assertText_Email'
        time.sleep(5)

    def test_assertText_Password(self):
        #Validate that the "Password" label is present.
        test_assertText_Password = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//label[@for='pseudonym_session_password']"))
        #print webElement.text
        assert test_assertText_Password.text == 'Password'
        print 'test_assertText_Password'
        time.sleep(5)

##Find and Validate Input Elements
    def test_FindElement_emailInput(self):
        #Validate that the Email element is present.
        test_FindElement_emailInput = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pseudonym_session_unique_id"))
        ##webElement = driver.find_element_by_id("pseudonym_session_unique_id")
        #webElement = driver.find_element_by_xpath("//input[@name='q']")
        #webElement = driver.find_element_by_css_selector("input[name=q]")
        #webElement = driver.find_element_by_name("q")
        ##webElement = driver.find_element_by_class_name("wsite-search-input")
        #print webElement
        print 'test_FindElement_emailInput'
        time.sleep(5)

    def test_FindElement_passwordInput(self):
        #Validate that the password element is present.
        test_FindElement_passwordInput = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pseudonym_session_password"))
        print 'test_FindElement_passwordInput'
        time.sleep(5)

##Find and Validate Canvas logo
    def test_FindElement_canvasLogo(self):
        #Validate that the canvas logo is present.
        test_FindElement_canvasLogo = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_css_selector("svg"))
        print 'test_FindElement_canvasLogo'
        time.sleep(5)


##Find and Validate Button Elements
    def test_FindAnElementButton_LogIn(self):
        #Validate that the "Log In" button is present.
        test_FindAnElementButton_LogIn = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[contains(.,'Log In')]"))
        #print webElement.text
        print 'test_FindAnElementButton_LogIn'
        time.sleep(5)

##Find and Validate Link Elements

    def test_FindAnElementLink_Browsecourses(self):
        #Find Element by link text "Browse courses"
        test_FindAnElementLink_Browsecourses = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Browse courses'))
        print 'test_FindAnElementLink_Browsecourses'
        time.sleep(5)

    def test_FindAnElementLink_ForgotPassword(self):
        #Find Element by link text "Forgot Password?"
        test_FindAnElementLink_ForgotPassword = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Forgot Password?'))
        print 'test_FindAnElementLink_ForgotPassword'
        time.sleep(5)

    def test_FindAnElementLink_UserResearch(self):
        #Find Element by link text "User Research"
        test_FindAnElementLink_UserResearch = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('User Research'))
        print 'test_FindAnElementLink_UserResearch'
        time.sleep(5)

    def test_FindAnElementLink_Help(self):
        #Find Element by link text "Help"
        test_FindAnElementLink_Help = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Help'))
        print 'test_FindAnElementLink_Help'
        time.sleep(5)

    def test_FindAnElementLink_Privacypolicy(self):
        #Find Element by link text "Privacy policy"
        test_FindAnElementLink_Privacypolicy = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Privacy policy'))
        print 'test_FindAnElementLink_Privacypolicy'
        time.sleep(5)

    def test_FindAnElementLink_Termsofservice(self):
        ##Find Element by link text "Terms of service"
        test_FindAnElementLink_Termsofservice = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Terms of service'))
        print 'test_FindAnElementLink_Termsofservice'
        time.sleep(5)

    def test_FindAnElementLink_Facebook(self):
        #Find Element by link text "Facebook"
        test_FindAnElementLink_Facebook = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Facebook'))
        print 'test_FindAnElementLink_Facebook'
        time.sleep(5)

    def test_FindAnElementLink_Twitter(self):
        #Find Element by link text "Twitter"
        test_FindAnElementLink_Twitter = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Twitter'))
        print 'test_FindAnElementLink_Twitter'
        time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
