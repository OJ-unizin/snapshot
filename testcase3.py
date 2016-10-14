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
class TestCase3(unittest.TestCase):
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


        #iframe Loading...
        #Loading = WebDriverWait, 10).until(lambda driver: driver.find_element_by_xpath("//div[@class='main-content loading']"))

        driver.switch_to_frame(1)
        #driver.switch_to_frame("iframe")
        print driver.title
        time.sleep(5)


        #Student Monitoring iframe menu link
        webElement_StudentMonitoring = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(.,'Student Monitoring')]"))
        print webElement_StudentMonitoring.text
        webElement_StudentMonitoring.click()
        time.sleep(5)


        #webElement_Comments = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//i[@class='icon-comments']"))
        webElement_Comments = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//span[@class='icon-comments style--icon--1JSx6']"))
        print webElement_Comments.text
        webElement_Comments.click()

        test = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//legend[contains(.,'Send us some feedback')]"))
        print test.text

        test1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//label[contains(.,'Please select a topic')]"))
        print test1.text

        webElement_dropdown = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//option[contains(.,'I really like...')]"))
        #webElement_dropdown = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//select[@id='field-5']"))
        print webElement_dropdown.text
        webElement_dropdown.click()
        webElement_text = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//textarea[@name='text']"))
        print webElement_text.text
        webElement_text.send_keys("I really like Unizin!!")
        time.sleep(5)


        #webElement_h1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//h1[contains(.,'[CMP Production] Template Course')]"))
        webElement_h2 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//h2[contains(.,'[CMP Production] Template Course')]"))
        print webElement_h2.text
        assert webElement_h2.text == '[CMP Production] Template Course'
        webElement_div = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[contains(@class,'discrete')]"))
        print webElement_div.text
        assert webElement_div.text == 'EAP 102 / Section #102 / 2 students'

        #Average Score
        webElement_test = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@class='style--avg-grade-summary--146yD']"))
        print webElement_test.text

        #webElement_test1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//i[contains(.,'Assignments')]"))
        #webElement_test1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@class='style--card-header-title--T2LUL bulma--card-header-title--1tYXO']"))
        #webElement_test1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[contains(.,'')]"))

        #filter by students name field
        webElement_test1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@type='text']"))
        #webElement_test1 = WebDriverWait(driver, 10).until(lambda driver: .style--charts--1qCmy > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > header:nth-child(1) > div:nth-child(1)
        print webElement_test1.text

        ##filters Red / Orange / Green
        webElement_test2 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[contains(@class,'style--student-filter--1Fkda')]"))
        print webElement_test2.text

        #Sort by
        webElement_test3 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//select[@id='sort-by']"))
        print webElement_test3.text

        #Per page
        webElement_test4 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//select[@id='per-page']"))
        print webElement_test4.text


        #Click the Send Feedback button
        #webElement_SendFeedbackbtn = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@type='submit']"))
        #Click X to close the Feedback form
        webElement_Comments.click()

        #Section Outcome iframe menu link
        #webElement_SectionOutcome = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(.,'Section Outcomes')]"))
        webElement_SectionOutcomesLink = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(.,'Section Outcomes')]"))
        print webElement_SectionOutcomesLink.text
        webElement_SectionOutcomesLink.click()


        #webElement_legal = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//p[contains(.,'Snapshot is a Unizin, Ltd product.')]"))

        webElement_legal = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[contains(.,'Help')]"))
        print webElement_legal.text
        #driver.switch_to.default_content()
        time.sleep(5)
        #cmpProductionCourse1_Element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//span[@class='name']"))



##        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        #browser.get_screenshot_as_file('screenshot-%s.png' % now)
##        driver.save_screenshot('screenshot-%s.jpg' % now)

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
