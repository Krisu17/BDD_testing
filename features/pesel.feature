Feature: PESEL Validation

    Scenario: Given PESEL is correct
        Given 84082995025 as a PESEL
        When validate PESEL
        Then receive 0 in return PESEL test

    Scenario: Given PESEL is too short
        Given 840829955 as a PESEL
        When validate PESEL
        Then receive 1 in return PESEL test

    Scenario: Given PESEL is too long
        Given 8408299502523 as a PESEL
        When validate PESEL
        Then receive 1 in return PESEL test

    Scenario: Given PESEL contains something other than digits
        Given 84082sa5025 as a PESEL
        When validate PESEL
        Then receive 2 in return PESEL test

    Scenario: Given PESEL is incorrect
        Given 84082995023 as a PESEL
        When validate PESEL
        Then receive 3 in return PESEL test