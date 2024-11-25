#Feature: Test Scenarios for off plan
#
#  Scenario: User can filter the off plan products by Unit price range
#    Given Open the main page
#    When Input user name
#    When Input user password
#    When Click continue button
#    Then Click on “off plan” at the left side menu
#    Then Verify the right page opens
#    And Click on filter
#    And Input products price from 1200000
#    And Input product price to 2000000
#    And Click on apply filter
#    Then Verify the price in all cards is inside the range 1200000 - 2000000



Feature: Test mobile Scenarios for off plan

  Scenario: User can filter the off plan products by Unit price range in mobile
    Given Open the main page mobile
    When Input user name mobile
    When Input user password mobile
    When Click continue button mobile
    Then Click on “off plan” at the left side menu mobile
    Then Verify the right page opens mobile
    And Click on filter mobile
    And Input products price from 1200000 mobile
    And Input product price to 2000000 mobile
    And Click on apply filter mobile
    Then Verify the price in all cards is inside the range 1200000 - 2000000 mobile

