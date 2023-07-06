@feature
Feature: Users
    Users feature

    Scenario: Check log in
        Given user opens index page
        When user logs in with credentials
        Then user successfull message is sent

    Scenario: Check nbp currencies
        Given user not logged
        When user opens currency page
        Then currencies are fetched
