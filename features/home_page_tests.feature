Feature: TigTag Home Page Tests

  Scenario: Go to How To Use page
    Given I navigate to the TwigWorld home page
    When I search for slime
    Then I am taken to the search results page