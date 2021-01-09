Feature: Login Validation

    Scenario: Given Login is correct
        Given testlogin as a Login
        When validate Login
        Then receive 0 in return Login test

    Scenario: Given too short Login
        Given log as a Login
        When validate Login
        Then receive 1 in return Login test

    Scenario: Given Login is not only letters
        Given log1n as a Login
        When validate Login
        Then receive 2 in return Login test
        
