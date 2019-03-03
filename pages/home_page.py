"""
HomePage Object
"""

import re

from selenium.webdriver.common.keys import Keys

from base_page import BasePage
from locators import HomePageLocators


class HomePage(BasePage):
    url = 'https://www.amazon.com'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.locator = HomePageLocators

    def navigate_to_cart(self):
        self.browser.find_element(*self.locator.CART).click()

    def navigate_to_prime(self):
        self.browser.find_element(*self.locator.PRIME).click()

    def set_search_query(self, product_query):
        search_box = self.browser.find_element(*self.locator.SEARCH_BOX)
        search_box.send_keys(product_query)
        search_box.send_keys(Keys.ENTER)
