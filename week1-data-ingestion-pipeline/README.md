# Week 1: Creating a data ingestion pipeline

## Adding environment variables

Rename `.env.template` into `.env` in the project root

## Setting up a postgres database + pgadmin

In project root, run:
* docker-compose up

## Connecting to the postgres database

Using `pgcli`: pgcli -h localhost -p `POSTGRES_PORT` -u `POSTGRES_USER` -d `POSTGRES_DB`

Using `pgadmin`: you can access it at localhost:72. add a new server with the name `pg-database` and the other variables from the `env` file. check https://youtu.be/hCAIVe9N0ow?t=541 if in doubt
