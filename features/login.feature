Feature: Login
  As a customer of the store
  I want to log in with my account
  So that I can see and buy products

  Background:
    Given the user is on the login page

  Scenario: Successful login with a valid user
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the products page is displayed

  Scenario Outline: Login is rejected with invalid data
    When the user logs in with username "<username>" and password "<password>"
    Then the error message "<message>" is displayed
    And the user stays on the login page

    Examples:
      | username        | password     | message                                                                   |
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                       |
      | standard_user   | wrong_pass   | Epic sadface: Username and password do not match any user in this service |
      |                 | secret_sauce | Epic sadface: Username is required                                        |
      | standard_user   |              | Epic sadface: Password is required                                        |
