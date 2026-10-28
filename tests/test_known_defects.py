from pytest_bdd import scenarios, then

scenarios("known_defects.feature")


@then("each product shows a different image")
def each_product_has_its_own_image(inventory_page):
    sources = inventory_page.get_image_sources()
    assert len(set(sources)) == len(sources), f"Repeated images: {sources}"
