from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_names = page.locator(".cart_item .inventory_item_name")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def get_names(self):
        return self.item_names.all_inner_texts()

    def start_checkout(self):
        self.checkout_button.click()
