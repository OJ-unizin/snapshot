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

    def test_assertText_Email(self):
        #Validate that the "Email" label is present.
        webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//label[@for='pseudonym_session_unique_id']"))
        #print webElement.text
        assert webElement.text == 'Email'


    def test_assertText_Password(self):
        #Validate that the "Password" label is present.
        webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//label[@for='pseudonym_session_password']"))
        #print webElement.text
        assert webElement.text == 'Password'

##Find and Validate Input Elements
    def test_FindElement_emailInput(self):
        #Validate that the Email element is present.
        webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pseudonym_session_unique_id"))
        ##webElement = driver.find_element_by_id("pseudonym_session_unique_id")
        #webElement = driver.find_element_by_xpath("//input[@name='q']")
        #webElement = driver.find_element_by_css_selector("input[name=q]")
        #webElement = driver.find_element_by_name("q")
        ##webElement = driver.find_element_by_class_name("wsite-search-input")
        #print webElement


    def test_FindElement_passwordInput(self):
        #Validate that the password element is present.
        webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pseudonym_session_password"))


##Find and Validate Canvas logo
    def test_FindElement_canvasLogo(self):
        #Validate that the canvas logo is present.
        webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_css_selector("svg"))



##Find and Validate Button Elements
    def test_FindAnElementButton_LogIn(self):
        #Validate that the "Log In" button is present.
        webElement_LogInbtn = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[contains(.,'Log In')]"))
        #print webElement.text

##Find and Validate Link Elements

    def test_FindAnElementLink_Browsecourses(self):
        #Find Element by link text "Browse courses"
        webElement_BrowseCourse = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Browse courses'))

    def test_FindAnElementLink_ForgotPassword(self):
        #Find Element by link text "Forgot Password?"
        webElement_ForgotPassword = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Forgot Password?'))

    def test_FindAnElementLink_UserResearch(self):
        #Find Element by link text "User Research"
        webElement_UserResearch = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('User Research'))

    def test_FindAnElementLink_Help(self):
        #Find Element by link text "Help"
        webElement_Help = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Help'))

    def test_FindAnElementLink_Privacypolicy(self):
        #Find Element by link text "Privacy policy"
        webElement_PrivacyPolicy = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Privacy policy'))

    def test_FindAnElementLink_Termsofservice(self):
        ##Find Element by link text "Terms of service"
        webElement_TermsofService = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Terms of service'))

    def test_FindAnElementLink_Facebook(self):
        #Find Element by link text "Facebook"
        webElement_Facebook = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Facebook'))

    def test_FindAnElementLink_Twitter(self):
        #Find Element by link text "Twitter"
        webElement_Twitter = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_link_text('Twitter'))


        time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
