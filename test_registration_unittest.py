from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, unittest


class TestAbs(unittest.TestCase):

    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('//input[@placeholder[contains(., "name")] and @class[contains(., "first")]]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath('//input[@placeholder[contains(., "name")] and @class[contains(., "second")]]')
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_xpath('//input[@placeholder[contains(., "email")] and @class[contains(., "third")]]')
        input3.send_keys("email")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")#WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1")))
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()
        
    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('//input[@placeholder[contains(., "name")] and @class[contains(., "first")]]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath('//input[@placeholder[contains(., "name")] and @class[contains(., "second")]]')
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_xpath('//input[@placeholder[contains(., "email")] and @class[contains(., "third")]]')
        input3.send_keys("email")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")#WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1")))
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()
