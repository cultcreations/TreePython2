from selenium.webdriver.common.by import By
from features.pages.page_base import *


class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "search")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='search-btn']")


class HomePage(PageBase):

    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)
