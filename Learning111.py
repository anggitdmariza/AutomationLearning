# Import the unittest module and the selenium module
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time


# Define a class that inherits from unittest.TestCase


class TestLogin(unittest.TestCase):

    # Define a setUp method that will create a WebDriver instance and navigate to the web page
    def setUp(self):
        self.driver = webdriver.Chrome('C:/chromedriver-win32/chromedriver.exe')
        self.driver.get('https://www.saucedemo.com')

    # Define a tearDown method that will quit the WebDriver instance
    def tearDown(self):
        self.driver.quit()

    # Define a test method that tests the incorrect login
    def test_case_incorrect_login(self):
        # Find the username and password fields and the login button
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")
        # Enter the username and password and click on the login button
        username_field.send_keys("locked_out_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        # Check if the login failed by verifying the error message
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = self.driver.find_element_by_css_selector(".error-message-container.error").text
        self.assertEqual(expected_error, actual_error, "The error message does not match")

    # Define a test method that tests the correct login
    def test_case_positive(self):

        """input correct username and password"""
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        '''check the menu'''
        self.driver.find_element_by_class_name('bm-burger-button').click()
        wait = WebDriverWait(self.driver, 2)
        cross_btn = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-cross-btn")))
        time.sleep(0.5)
        cross_btn.click()

        '''check footer'''
        expected_footer = '© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy'
        actual_footer = self.driver.find_element(By.CLASS_NAME, 'footer_copy').text
        assert expected_footer == actual_footer

        '''check inventories sorter'''
        index = 0
        for i in range(3):
            index = index + 1
            sorter = self.driver.find_element_by_xpath("//select[@class='product_sort_container']")
            Select(sorter).select_by_index(index)
        self.driver.find_element_by_class_name('inventory_item_img').click()
        self.driver.find_element_by_id('back-to-products').click()

        '''choose product(s)'''
        add_to_cart_bt = self.driver.find_elements_by_class_name("btn_inventory")
        for bt in add_to_cart_bt[:2]:
            bt.click()

        '''open cart'''
        cart_link = self.driver.find_elements_by_class_name("shopping_cart_link")
        for bt in cart_link:
            bt.click()
        self.driver.find_element_by_id('checkout').click()

        '''filling form'''
        self.driver.find_element_by_id('first-name').send_keys('Sauce')
        self.driver.find_element_by_id('last-name').send_keys('Demo')
        self.driver.find_element_by_id('postal-code').send_keys('111')
        self.driver.find_element_by_id('continue').click()

        '''payment confirmation'''
        self.driver.find_element(By.CLASS_NAME, 'cart_list').is_displayed()
        self.driver.find_element(By.CLASS_NAME, 'summary_info').is_displayed()
        self.driver.find_element(By.ID, 'finish').click()
        self.driver.find_element(By.ID, 'checkout_complete_container').is_displayed()

    def test_failed_filling(self):
        """input correct username and password"""
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        '''check the menu'''
        self.driver.find_element_by_class_name('bm-burger-button').click()
        wait = WebDriverWait(self.driver, 2)
        cross_btn = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-cross-btn")))
        time.sleep(0.5)
        cross_btn.click()

        '''check footer'''
        expected_footer = '© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy'
        actual_footer = self.driver.find_element(By.CLASS_NAME, 'footer_copy').text
        assert expected_footer == actual_footer

        '''check inventories sorter'''
        index = 0
        for i in range(3):
            index = index + 1
            sorter = self.driver.find_element_by_xpath("//select[@class='product_sort_container']")
            Select(sorter).select_by_index(index)
        self.driver.find_element_by_class_name('inventory_item_img').click()
        self.driver.find_element_by_id('back-to-products').click()

        '''choose product(s)'''
        add_to_cart_bt = self.driver.find_elements_by_class_name("btn_inventory")
        for bt in add_to_cart_bt[:2]:
            bt.click()

        '''open cart'''
        cart_link = self.driver.find_elements_by_class_name("shopping_cart_link")
        for bt in cart_link:
            bt.click()
        self.driver.find_element_by_id('checkout').click()

        '''empty form'''
        self.driver.find_element(By.ID, 'continue').click()
        error_message = 'Error: First Name is required'
        actual_message = self.driver.find_element(By.XPATH, "//h3[normalize-space()"
                                                            "='Error: First Name is required']").text
        assert error_message == actual_message


# Add a main block that will run the tests using unittest.main()
if __name__ == "__main__":
    unittest.main()
