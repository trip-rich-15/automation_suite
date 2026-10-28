from playwright.sync_api import expect
from pytest_bdd import parsers, scenarios, then, when

scenarios("checkout.feature")


@then(parsers.parse('the item total is "{total}"'))
def item_total_is(checkout_page, total):
    expect(checkout_page.item_total).to_have_text(total)


@when("the user finishes the purchase")
def finish_purchase(checkout_page):
    checkout_page.finish()


@then(parsers.parse('the confirmation message "{message}" is displayed'))
def confirmation_is_displayed(checkout_page, message):
    expect(checkout_page.complete_header).to_have_text(message)


@then("the cart is empty")
def cart_is_empty(checkout_page):
    expect(checkout_page.cart_badge).to_have_count(0)
