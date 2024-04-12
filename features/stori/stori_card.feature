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
  Scenario: Verify select options from dropdown example
    Given I navigate to the AutomationPractice main page
    When I selects option 2
    And Then the option 3 in the dropdown example
    Then I verifies the change in the selection

  @test2
  Scenario: Verify text in popup window
    Given I navigate to the AutomationPractice main page
    When I click on the Open Window button in the Switch Window Example
    Then I verifies that the "30 day money back guarantee" text is displayed

  @test3
  Scenario: check navigation and capture screen in new tab
    Given I navigate to the AutomationPractice main page
    When I click the Open tab button in the example tab change
    And I navigates to the origin page tab and finds the button
    Then I captures a screenshot that includes the button and saves it with the test case name

  @test4
  Scenario: verify interact with alerts
    Given I navigate to the AutomationPractice main page
    And type the string "Stori Card" in the example Change to alert
    When I accept the alert and verify the text
    And I repeat the process for the confirmation alert
    Then I verify that the text that is printed in the alert and confirmation are the same as the string "".

  @test5
  Scenario: Interacting with web table
    Given I navigate to the AutomationPractice main page
    When I analyze the courses that cost $25 and $15 in the web table
    Then I print the names of the courses and their corresponding prices

  @test6
  Scenario: Verify the names of the engineers
    Given I navigate to the AutomationPractice main page
    When I identify the names of the Engineers and Businessman in the web table
    Then I print the names identifying the role
