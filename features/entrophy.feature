Feature: Entrophy Validation

    Scenario: Given Entrophy is very low
        Given ha as a Entrophy
        When validate Entrophy
        Then receive 0 in return Entrophy test

    Scenario: Given Entrophy is low
        Given haslo as a Entrophy
        When validate Entrophy
        Then receive 1 in return Entrophy test

    Scenario: Given Entrophy is medium
        Given haslo1 as a Entrophy
        When validate Entrophy
        Then receive 2 in return Entrophy test

    Scenario: Given Entrophy is high
        Given haslo123 as a Entrophy
        When validate Entrophy
        Then receive 3 in return Entrophy test

    Scenario: Given Entrophy is very high
        Given haslo123!@#$ as a Entrophy
        When validate Entrophy
        Then receive 4 in return Entrophy test