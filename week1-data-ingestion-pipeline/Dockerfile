FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
COPY .env .env

COPY ./data/raw_data/green_tripdata_2019-09.csv.gz green_tripdata_2019-09.csv.gz
COPY ./data/raw_data/taxi+_zone_lookup.csv taxi+_zone_lookup.csv

COPY week1-data-ingestion-pipeline/data_ingestion.py data_ingestion.py

RUN pip install -r requirements.txt

CMD 


