Feature: Test Scenarios for off plan

  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    When Input user name
    When Input user password
    When Click continue button
    Then Click on “off plan” at the left side menu
    Then Verify the right page opens
    And Click on filter
    And Input products price from 1200000
    And Input product price to 2000000
    And Click on apply filter
    Then Verify the price in all cards is inside the range 1200000 - 2000000
