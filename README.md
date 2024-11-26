# Lab 10 - Airflow Practice

Get hands-on experience with Apache Airflow


## Table of Contents

This repository contains 2 projects for demonstrating the capabilities and use cases of Airflow.

- [ETL](etl/README.md) A project for learning the basics of ETL with Airflow
- [Learning Airflow](learning-airflow/README.md) A project for learning the basics of Airflow

## Purpose of This Repository
These templates are designed to help new users learn and try Airflow quickly. 

## Pre-requisites:

1. Docker Desktop
2. Install the `astro` CLI from Astronomer.io. Follow [these instructions](https://www.astronomer.io/docs/astro/cli/install-cli/) for your platform.

## Run Airflow Locally

1. Clone this project and navigate to the `learning-airflow` project subdirectory.

2. Start Airflow for that project on your local machine by running `astro dev start` from within that directory.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

3. Verify that all 4 Docker containers were created by running `docker ps`.

Note: Running `astro dev start` will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

4. Access the Airflow UI for your local Airflow project. To do so, go to `http://localhost:8080/` and log in with `admin` for both your Username and Password.

You should also be able to access your Postgres Database at `localhost:5432/postgres`.

## Add your own DAG

1. Within the Airflow UI, go to the Admin-->Variables from the top navigation menu.
2. Create one variable entry (key-value pair):
    - MONGOPASS - assigned the value given to you in the instruction page.
3. Add a new file `simple.py` within the `dags` subdirectory of the project. The code for this page can be found at
4. Update the BUCKET variable in the code to `xxxxx`.
5. Update the DB variable in the code to your UVA computing ID.
6. Save the file and return to the Airflow UI. Refresh the page or wait a couple of minutes for your DAG to appear. It should be in a paused state.
7. Unpause your DAG and run it once by hand.
8. You can use `MONGO-ATLAS` from your fork of the [`mongodb-practice` repository](https://github.com/nmagee/mongodb-practice/) to review the values your code inserted into the database. Be sure to select the correct database.
9. Take a screenshot of the inserted document in MongoDB and submit it for the lab.

## Cleaning Up

When done, issue the command `astro dev stop` to turn off the Docker stack.
