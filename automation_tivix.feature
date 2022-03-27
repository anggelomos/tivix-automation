Feature: Car rent

  @critical_test
  Scenario: Rent a car successfully
    Given that I am on the main rent page
    When I do the process to rent a car
    Then I rent a car successfully