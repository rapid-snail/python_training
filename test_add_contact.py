# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("first name")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("middlename")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("lastname")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("nickname")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("company")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("address")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("home phone")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("mobile phone")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("work phone")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("fax")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("email1")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("email2")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("email3")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("homepage")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("March")
        driver.find_element_by_xpath("//option[@value='March']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1970")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("2")
        driver.find_element_by_xpath("(//option[@value='2'])[2]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("December")
        driver.find_element_by_xpath("(//option[@value='December'])[2]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1980")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("secondary address")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("secondary home")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("notes")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
