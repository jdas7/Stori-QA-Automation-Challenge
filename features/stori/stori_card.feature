@Regression-tests
Feature: Stori QA Automation Engineer Challenge

  @smoke-test
  Scenario: validation test page
    Given I access the page "https://rahulshettyacademy.com/AutomationPractice/"
    Then I see the option Suggession Class Example

  @test0
  Scenario Outline: verify select countries option
    Given I navigate to the AutomationPractice main page
    When I enter the word "<word>" in the option Suggession Class Example
    Then I select the country "<country>" correctly

    Examples:
      | word | country                |
      | Me   | México                 |
      | Uni  | Estados Unidos         |
      | Uni  | Emiratos Árabes Unidos |
      | Col  | Colombia               |

  @test1
  Scenario: Select options from dropdown example
    Given I navigate to the AutomationPractice main page
    When The user selects option 2
    And Then the option option 3 in the dropdown example
    Then User verifies the change in the selection

  