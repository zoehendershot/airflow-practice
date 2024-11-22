from airflow import Dataset
from airflow.decorators import (
    dag,
    task,
) 
from pendulum import datetime, duration
import requests

# -------------- #
# DAG Definition #
# -------------- #

@dag(
    start_date=datetime(2024, 1, 1),
    schedule='* * * * *',
    catchup=False,
    max_consecutive_failed_dag_runs=3,
    doc_md=__doc__,
    default_args={
        "owner": "Neal",
        "retries": 3,
        "retry_delay": duration(seconds=5),
    }, 
    tags=["example", "humor"],
    is_paused_upon_creation=False
)
def simple():

    @task(outlets=[Dataset("simple")])

    def get_jokes(**context) -> list[dict]:
        try:
            r = requests.get("https://official-joke-api.appspot.com/random_joke")
            r.raise_for_status()
            setup = r.json()["setup"]
            punchline = r.json()["punchline"]
            print(setup, punchline)
        except:
            print("API currently not available.")

        return setup, punchline

    # @task
    # def print_astronaut_craft(greeting: str, person_in_space: dict) -> None:
    #     craft = person_in_space["craft"]
    #     name = person_in_space["name"]

    #     print(f"{name} is in space flying on the {craft}! {greeting}")


simple()
