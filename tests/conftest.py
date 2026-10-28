import re

import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, then, when

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"


# Page objects

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


# Shared steps

@given(parsers.parse('the user is logged in as "{username}"'))
def logged_in_as(login_page, inventory_page, username):
    login_page.open()
    login_page.login(username, PASSWORD)
    expect(inventory_page.title).to_have_text("Products")


@then(parsers.parse('the error message "{message}" is displayed'))
def error_message_is_displayed(page, message):
    expect(BasePage(page).error_message).to_have_text(message)


@given(parsers.parse('the user adds "{product}" to the cart'))
@when(parsers.parse('the user adds "{product}" to the cart'))
def add_product(inventory_page, product):
    inventory_page.add_to_cart(product)


@given("the user goes to the cart")
@when("the user goes to the cart")
def go_to_cart(inventory_page):
    inventory_page.go_to_cart()


@given("the user starts the checkout")
@when("the user starts the checkout")
def start_checkout(cart_page):
    cart_page.start_checkout()


# The values can be empty, so a regular expression is used instead of parsers.parse
@when(parsers.re(
    r'the user enters first name "(?P<first_name>[^"]*)", '
    r'last name "(?P<last_name>[^"]*)" and postal code "(?P<postal_code>[^"]*)"'
))
def enter_information(checkout_page, first_name, last_name, postal_code):
    checkout_page.fill_information(first_name, last_name, postal_code)


@when("the user continues to the overview")
def continue_to_overview(checkout_page):
    checkout_page.continue_to_overview()


@then("the checkout overview is displayed")
def overview_is_displayed(page):
    expect(page).to_have_url(re.compile(r".*/checkout-step-two\.html"))


@when(parsers.parse('the user sorts the products by "{option}"'))
def sort_products(inventory_page, option):
    inventory_page.sort_by(option)


@then(parsers.parse('the products are sorted by "{option}"'))
def products_are_sorted(inventory_page, option):
    if option.startswith("Name"):
        values = inventory_page.get_names()
    else:
        values = inventory_page.get_prices()

    descending = option in ("Name (Z to A)", "Price (high to low)")
    assert values == sorted(values, reverse=descending), f"Wrong order for '{option}': {values}"
