from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.item_images = page.locator(".inventory_item img")
        self.sort_select = page.locator(".product_sort_container")

    def item(self, product_name):
        return self.items.filter(has_text=product_name)

    def add_to_cart(self, product_name):
        self.item(product_name).get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, product_name):
        self.item(product_name).get_by_role("button", name="Remove").click()

    def sort_by(self, option):
        self.sort_select.select_option(label=option)

    def get_names(self):
        return self.item_names.all_inner_texts()

    def get_prices(self):
        return [float(price.replace("$", "")) for price in self.item_prices.all_inner_texts()]

    def get_image_sources(self):
        return [image.get_attribute("src") for image in self.item_images.all()]
