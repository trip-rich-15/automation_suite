from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Step one: customer information
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        # Step two: overview
        self.item_total = page.locator(".summary_subtotal_label")
        self.finish_button = page.locator('[data-test="finish"]')
        # Complete
        self.complete_header = page.locator(".complete-header")

    def fill_information(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()
