from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.error_message = page.locator('[data-test="error"]')
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def go_to_cart(self):
        self.cart_link.click()
