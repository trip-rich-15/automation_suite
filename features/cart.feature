Feature: Shopping cart
  As a customer
  I want to add and remove products in my cart
  So that I can choose what I want to buy

  Background:
    Given the user is logged in as "standard_user"

  Scenario: Add a product to the cart
    When the user adds "Sauce Labs Backpack" to the cart
    Then the cart badge shows "1"

  Scenario: Remove a product from the cart
    When the user adds "Sauce Labs Backpack" to the cart
    And the user adds "Sauce Labs Bike Light" to the cart
    And the user removes "Sauce Labs Backpack" from the cart
    Then the cart badge shows "1"

  Scenario: The cart shows the added products
    When the user adds "Sauce Labs Backpack" to the cart
    And the user adds "Sauce Labs Bike Light" to the cart
    And the user goes to the cart
    Then the cart contains "Sauce Labs Backpack"
    And the cart contains "Sauce Labs Bike Light"
