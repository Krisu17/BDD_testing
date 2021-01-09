Feature: Email Validation

    Scenario: Given Email is correct
        Given pawel@pawel.com as a Email
        When I test validity of Email
        Then I get 0 in return

    Scenario: Given Email without at
        Given pawel as a Email
        When I test validity of Email
        Then I get 1 in return

    Scenario: Given Email starts with at
        Given @pawel as a Email
        When I test validity of Email
        Then I get 2 in return

    Scenario: Given Email ends with at
        Given pawel@ as a Email
        When I test validity of Email
        Then I get 3 in return

    Scenario: Given Email without domain
        Given pawel@pawel as a Email
        When I test validity of Email
        Then I get 4 in return

    
