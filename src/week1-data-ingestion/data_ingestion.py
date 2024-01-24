import os
from argparse import ArgumentParser, Namespace

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from tqdm import tqdm


def main(args: Namespace):
    assert os.path.exists(args.csv_path), f"Data not found at {args.csv_path}"

    engine = create_engine(f"postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}")

    df = pd.read_csv(args.csv_path, nrows=1)
    df.head(n=0).to_sql(name=args.table_name, con=engine, if_exists="replace")

    df_iter = pd.read_csv(args.csv_path, iterator=True, chunksize=100000)
    
    for item in tqdm(df_iter):
        item.to_sql(name=args.table_name, con=engine, if_exists='append')

if __name__ == "__main__":
    load_dotenv(".env")

    parser = ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument("--csv_path", default="./data/raw_data/green_tripdata_2019-01.csv.gz", help="path to the csv file")
    parser.add_argument(
        "--user", "--u", default=os.getenv("POSTGRES_USER", ""), help="user name for postgres"
    )
    parser.add_argument(
        "--password", "--p", default=os.getenv("POSTGRES_PASS", ""), help="password for postgres"
    )
    parser.add_argument("--host", default=os.getenv("POSTGRES_HOST", ""), help="host for postgres")
    parser.add_argument("--port", default=os.getenv("POSTGRES_PORT", ""), help="port for postgres")
    parser.add_argument(
        "--db", "--database", default=os.getenv("POSTGRES_DB", ""), help="database name for postgres"
    )
    parser.add_argument("--table_name", default="green_trip_data", help="name of the table where we will write the results to")

    args = parser.parse_args()

    if not (args.user and args.password and args.host and args.port and args.db):
        print("Fill in the .env according to the template or provide the postgres connection variables")
        exit(1)

    main(args)
