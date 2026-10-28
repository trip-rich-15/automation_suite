Feature: Checkout
  As a customer
  I want to complete my purchase
  So that I can receive my products

  Background:
    Given the user is logged in as "standard_user"
    And the user adds "Sauce Labs Backpack" to the cart
    And the user goes to the cart
    And the user starts the checkout

  Scenario: Complete a purchase from login to confirmation
    When the user enters first name "Ana", last name "Lopez" and postal code "9410"
    And the user continues to the overview
    Then the item total is "Item total: $29.99"
    When the user finishes the purchase
    Then the confirmation message "Thank you for your order!" is displayed
    And the cart is empty

  Scenario Outline: Customer information is required
    When the user enters first name "<first_name>", last name "<last_name>" and postal code "<postal_code>"
    And the user continues to the overview
    Then the error message "<message>" is displayed

    Examples:
      | first_name | last_name | postal_code | message                        |
      |            | Lopez     | 9410        | Error: First Name is required  |
      | Ana        |           | 9410        | Error: Last Name is required   |
      | Ana        | Lopez     |             | Error: Postal Code is required |
