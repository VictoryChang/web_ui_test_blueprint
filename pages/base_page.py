"""
BasePage Object
"""


class BasePage(object):
    url = None

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 30

    def navigate(self):
        self.browser.get(self.url)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def get_title(self):
        return self.browser.title
