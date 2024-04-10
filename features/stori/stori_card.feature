@Regression-tests
Feature: Stori QA Automation Engineer Challenge

  @smoke-test
  Scenario: validation test page
    Given I access the page "https://rahulshettyacademy.com/AutomationPractice/"
    Then I see the option Suggession Class Example

  Scenario Outline: verify select countries option
    Given I navigate to the AutomationPractice main page
    When I enter the word "<word>" in the option Suggession Class Example
    Then I select the country "<country>" correctly

    Examples:
      | word | country                |
      | Me   | México                 |
      | Uni  | Estados Unidos         |
      | Uni  | Emiratos Árabes Unidos |


  