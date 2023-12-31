@etl @e2e @ignore
Feature: Data Lake ETL jobs
    Data Lake ETL jobs for data analytics

    Scenario: Data is transfered from database to data lake

        Given prepared order in orders database
        When data lake ingestion is triggered
        Then data is published to message broker topic
        Then data is stored in raw zone
        Then transformation runs
        Then data is stored in trusted zone
        Then report is published
