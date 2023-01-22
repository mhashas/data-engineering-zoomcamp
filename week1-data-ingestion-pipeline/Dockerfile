FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
COPY .env .env
COPY ./data/raw_data/green_tripdata_2019-01.csv.gz green_tripdata_2019-01.csv.gz
COPY week1-data-ingestion-pipeline/data_ingestion.py data_ingestion.py

RUN pip install -r requirements.txt
RUN ls -lh

ENTRYPOINT ["python", "data_ingestion.py"]
CMD 


