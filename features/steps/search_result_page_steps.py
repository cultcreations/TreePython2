from behave import *
from nose.tools import assert_equal, assert_true

from features.pages.searchresults_page import SearchResultsPageLocator


@step('I am taken to the search results page')
def step_impl(context):
    searchtext = context.searchresults_page.findelementtext(*SearchResultsPageLocator.SEARCH_RESULT)
    assert_equal(searchtext, "Making Slime")
