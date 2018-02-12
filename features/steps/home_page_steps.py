from behave import *
from nose.tools import assert_equal, assert_true

from features.pages.home_page import HomePageLocator


@step('I navigate to the TwigWorld home page')
def step_impl(context):
    context.home_page.navigate("https://www.twig-world.com")
    assert_equal(context.home_page.get_page_title(), "Twig - Educational resources for KS3 Science")


@step('I search for slime')
def step_impl(context, *locator):
    context.home_page.search("Slime")
