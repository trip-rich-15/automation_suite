Feature: Product sorting
  As a customer
  I want to sort the products
  So that I can find what I need faster

  Background:
    Given the user is logged in as "standard_user"

  Scenario Outline: Products are sorted by the selected option
    When the user sorts the products by "<option>"
    Then the products are sorted by "<option>"

    Examples:
      | option              |
      | Name (A to Z)       |
      | Name (Z to A)       |
      | Price (low to high) |
      | Price (high to low) |
