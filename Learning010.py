from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SauceDemo:
    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver-win32\chromedriver.exe')
        self.driver.get('https://www.saucedemo.com')
        actual_title = self.driver.title
        expected_title = 'Swag Labs'
        assert expected_title == actual_title

    def positive_case(self):

        '''input correct username and password'''
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

        '''filling address'''
        self.driver.find_element_by_id('first-name').send_keys('Sauce')
        self.driver.find_element_by_id('last-name').send_keys('Demo')
        self.driver.find_element_by_id('postal-code').send_keys('111')
        self.driver.find_element_by_id('continue').click()

        '''payment confirmation'''
        self.driver.find_element(By.CLASS_NAME, 'cart_list').is_displayed()
        self.driver.find_element(By.CLASS_NAME, 'summary_info').is_displayed()
        self.driver.find_element(By.ID, 'finish').click()
        self.driver.find_element(By.ID, 'checkout_complete_container').is_displayed()


SauceDemo().positive_case()
time.sleep(0.5)
