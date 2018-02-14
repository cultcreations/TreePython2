from selenium import webdriver
from features.browser import *
from features.pages.home_page import HomePage
from features.pages.searchresults_page import SearchResultsPage


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.set_page_load_timeout(30)
driver.maximize_window()


def before_all(context):
    # Add all pages here so that they will be created during the test runs
    context.home_page = HomePage(driver)
    context.searchresults_page = SearchResultsPage(driver)


def after_all(context):
    driver.close()
