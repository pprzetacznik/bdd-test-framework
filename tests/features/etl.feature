@etl @e2e @ignore
Feature: ETL jobs
    ETL jobs for data analytics

    Scenario: Data is transfered from database to data lake

        Given prepared order in orders database
        When data warehouse ingestion is triggered
        Then data is published to message broker topic
        Then data is stored in raw zone
        Then transformation runs
        Then data is stoed in trusted zone
        Then report is published
