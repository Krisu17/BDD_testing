Feature: Password Validation

    Scenario: Given Password is correct
        Given qwertY12# as a Password
        When validate Password
        Then receive 0 in return Password test

    Scenario: Given Password is too short
        Given 1234567 as a Password
        When validate Password
        Then receive 1 in return Password test

    Scenario: Given Password does not contain upper
        Given 12345abc as a Password
        When validate Password
        Then receive 2 in return Password test

    Scenario: Given Password does not contain lower
        Given 12345ABC as a Password
        When validate Password
        Then receive 3 in return Password test

    Scenario: Given Password does not contain digit
        Given abcdEFGH as a Password
        When validate Password
        Then receive 4 in return Password test

    Scenario: Given Password does not contain special symbol
        Given 12345ABcd as a Password
        When validate Password
        Then receive 5 in return Password test