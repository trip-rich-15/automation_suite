from playwright.sync_api import expect
from pytest_bdd import parsers, scenarios, then, when

scenarios("cart.feature")


@when(parsers.parse('the user removes "{product}" from the cart'))
def remove_product(inventory_page, product):
    inventory_page.remove_from_cart(product)


@then(parsers.parse('the cart badge shows "{count}"'))
def cart_badge_shows(inventory_page, count):
    expect(inventory_page.cart_badge).to_have_text(count)


@then(parsers.parse('the cart contains "{product}"'))
def cart_contains(cart_page, product):
    assert product in cart_page.get_names()
