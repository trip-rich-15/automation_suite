import re

from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("login.feature")


@given("the user is on the login page")
def open_login_page(login_page):
    login_page.open()


# The values can be empty, so a regular expression is used instead of parsers.parse
@when(parsers.re(r'the user logs in with username "(?P<username>[^"]*)" and password "(?P<password>[^"]*)"'))
def log_in(login_page, username, password):
    login_page.login(username, password)


@then("the products page is displayed")
def products_page_is_displayed(page, inventory_page):
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(inventory_page.title).to_have_text("Products")


@then("the user stays on the login page")
def stays_on_login_page(login_page):
    expect(login_page.login_button).to_be_visible()
