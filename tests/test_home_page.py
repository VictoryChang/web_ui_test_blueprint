import unittest
from selenium import webdriver

from pages.home_page import HomePage


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.driver = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()


class HomePageTest(TestTemplate):
    def test_page_title_is_correct(self):
        homepage = HomePage(self.browser)
        homepage.navigate()
        title = homepage.get_title()
        assert 'Amazon.com: Online Shopping' in title

    def test_navigate_to_cart(self):
        homepage = HomePage(self.browser)
        homepage.navigate()
        homepage.navigate_to_cart()
        title = homepage.get_title()
        assert 'Amazon.com Shopping Cart' == title

    def test_navigate_to_prime(self):
        homepage = HomePage(self.browser)
        homepage.navigate()
        homepage.navigate_to_prime()
        title = homepage.get_title()
        assert 'Amazon.com: Amazon Prime' == title

    def test_product_search(self):
        homepage = HomePage(self.browser)
        homepage.navigate()
        homepage.set_search_query('ukulele')
        title = homepage.get_title()
        assert 'Amazon.com: ukulele' == title
