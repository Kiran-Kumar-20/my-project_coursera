Feature: Product Management
  As a user
  I want to manage products
  So that I can track inventory

  Scenario: List all products
    When I visit the "/products" endpoint
    Then I should see a list of products

  Scenario: Create a new product
    Given the following products
      | name       | category  | price | availability |
      | TestProduct| TestCat   | 10.99 | true         |
    When I send a POST request to "/products"
    Then the response status should be "201"

  Scenario: Search by name
    Given the following products
      | name       | category  | price | availability |
      | TestProduct| TestCat   | 10.99 | true         |
    When I visit the "/products?name=TestProduct" endpoint
    Then I should see a list of products
