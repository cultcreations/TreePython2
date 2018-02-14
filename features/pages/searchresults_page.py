from selenium.webdriver.common.by import By
from features.pages.page_base import *


class SearchResultsPageLocator(object):
    # Search Results Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_RESULT = (By.CSS_SELECTOR, "[class='search-info__title violet']")


class SearchResultsPage(PageBase):

    # Search Results Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def find_element_text(self, *locator):
        element_text = self.driver.find_element(*locator).text
        return element_text
