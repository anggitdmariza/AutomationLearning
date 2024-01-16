import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
# logging.basicConfig()
logger = logging.getLogger('testlog.log')
logger.setLevel(logging.INFO)
handlr = logging.StreamHandler()
logger.addHandler(handlr)


class TestSauceDemo(unittest.TestCase):
    driver = webdriver.Chrome('C:/chromedriver-win32/chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.get('https://www.saucedemo.com')
        cls.driver.maximize_window()

    def setUp(self):
        """Maybe pre-requisites"""
        """input correct username and password"""
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

    def tearDown(self):
        self.driver.find_element(By.CLASS_NAME, 'bm-burger-button').click()
        wait_ = WebDriverWait(self.driver, 10)
        wait_.until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
        self.driver.find_element(By.ID, 'logout_sidebar_link').click()
        expected_title = 'Swag Labs'
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title, 'Not Title')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shopping(self):
        """check the menu"""
        self.driver.find_element_by_class_name('bm-burger-button').click()
        wait_ = WebDriverWait(self.driver, 10)
        wait_.until(EC.element_to_be_clickable((By.ID, 'react-burger-cross-btn')))
        time.sleep(1)
        logger.info('Why still need time after waiting and confirmation?')
        self.driver.find_element(By.ID, 'react-burger-cross-btn').click()

        '''check footer'''
        expected_footer = '© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy'
        actual_footer = self.driver.find_element(By.CLASS_NAME, 'footer_copy').text
        self.assertEqual(expected_footer, actual_footer, 'Not Equal')

        '''check inventories sorter'''
        index = 0
        for i in range(3):
            index = index+1
            sorter = self.driver.find_element_by_xpath("//select[@class='product_sort_container']")
            Select(sorter).select_by_index(index)

        self.driver.find_element_by_class_name('inventory_item_img').click()
        self.driver.find_element(By.ID, 'back-to-products').click()

        '''choose product(s)'''
        add_to_cart_bt = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for bt in add_to_cart_bt[:2]:
            bt.click()

        '''open cart'''
        cart_link = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_link")
        for bt in cart_link:
            bt.click()
        self.driver.find_element(By.ID, 'checkout').click()

        '''filling address'''
        self.driver.find_element(By.ID, 'first-name').send_keys('Sauce')
        self.driver.find_element(By.ID, 'last-name').send_keys('Demo')
        self.driver.find_element(By.ID, 'postal-code').send_keys('111')
        self.driver.find_element(By.ID, 'continue').click()

        '''payment confirmation'''
        self.driver.find_element(By.CLASS_NAME, 'cart_list').is_displayed()
        self.driver.find_element(By.CLASS_NAME, 'summary_info').is_displayed()
        self.driver.find_element(By.ID, 'finish').click()

        '''Thank You Page'''
        act_ty = self.driver.find_element(By.CLASS_NAME, 'complete-header').text
        ec_ty = 'Thank you for your order!'
        assert ec_ty == act_ty
        self.driver.find_element(By.ID, 'back-to-products').click()

    def test_blank_filling(self):
        """check the menu"""
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
            index = index+1
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
