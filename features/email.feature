Feature: Email Validation

    Scenario: Given Email is correct
        Given pawel@pawel.com as a Email
        When validate Email
        Then receive 0 in return Email test

    Scenario: Given Email without at
        Given pawel as a Email
        When validate Email
        Then receive 1 in return Email test

    Scenario: Given Email starts with at
        Given @pawel as a Email
        When validate Email
        Then receive 2 in return Email test

    Scenario: Given Email ends with at
        Given pawel@ as a Email
        When validate Email
        Then receive 3 in return Email test

    Scenario: Given Email without domain
        Given pawel@pawel as a Email
        When validate Email
        Then receive 4 in return Email test