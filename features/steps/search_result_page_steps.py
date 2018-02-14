from behave import *
from nose.tools import assert_equal, assert_true

from features.pages.searchresults_page import SearchResultsPageLocator


@step('I am taken to the search results page')
def step_impl(context):
    search_text = context.searchresults_page.find_element_text(*SearchResultsPageLocator.SEARCH_RESULT)
    assert_equal(search_text, "Making Slime")
