Feature: Known defects with problem_user
  These scenarios check the expected behavior for the problem_user account.
  They fail because of open defects, so they are marked with a known_bug tag.
  If a defect is fixed, the scenario passes and the pipeline asks for a review.

  Background:
    Given the user is logged in as "problem_user"

  @known_bug_SD-01
  Scenario: Each product shows its own image
    Then each product shows a different image

  @known_bug_SD-02
  Scenario: Products can be sorted by price
    When the user sorts the products by "Price (low to high)"
    Then the products are sorted by "Price (low to high)"

  @known_bug_SD-03
  Scenario: The customer can enter the checkout information
    When the user adds "Sauce Labs Backpack" to the cart
    And the user goes to the cart
    And the user starts the checkout
    And the user enters first name "Ana", last name "Lopez" and postal code "9410"
    And the user continues to the overview
    Then the checkout overview is displayed
