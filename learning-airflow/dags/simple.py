from airflow import Dataset
from airflow.decorators import (
    dag,
    task,
) 
from airflow.models import Variable
from pendulum import datetime, duration
import requests
from pymongo import MongoClient, errors
from bson.json_util import dumps


MONGOPASS = Variable.get('MONGOPASS')

uri = "mongodb+srv://cluster0.m3fek.mongodb.net/"
client = MongoClient(uri, username='ds2022', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.nem2p  # database
flights = db.flights     # collection 

# -------------- #
# DAG Definition #
# -------------- #

@dag(
    start_date=datetime(2024, 1, 1),
    schedule='0 0 * * *',
    catchup=False,
    max_consecutive_failed_dag_runs=3,
    doc_md=__doc__,
    default_args={
        "owner": "ds2022",
        "retries": 3,
        "retry_delay": duration(seconds=5),
    }, 
    tags=["example","s3","etl"],
    is_paused_upon_creation=True
)
def simple():

    @task()
    def get_file(**context):
        try:
            r = requests.get("https://s3.amazonaws.com/ds2022-resources/airflow/data/flights.json")
            r.raise_for_status()
            dlfileval = r.json()
            context["ti"].xcom_push(key="dlfile", value=dlfileval)
        except:
            print("File currently unavailable.")


    @task
    def insert_mongo(xcom_received, **context):
        dlfileval = context["ti"].xcom_pull(key="dlfile")
        flights.insert_many(dlfileval)
        print("Flight records added to Mongo")

    insert_mongo(get_file())

simple()
