@feature
Feature: Users
    Users feature

    Scenario: Check log in
        Given user opens index page
        When user logs in with credentials
        Then user successfull message is sent
