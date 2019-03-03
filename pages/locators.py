"""
Locators
"""

from selenium.webdriver.common.by import By


class HomePageLocators(object):
    CART = (By.ID, 'nav-cart')
    PRIME = (By.ID, 'nav-link-prime')
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')