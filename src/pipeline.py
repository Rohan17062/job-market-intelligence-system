import pandas as pd
import random
from datetime import datetime, timedelta

def run_pipeline(conn):

    df = pd.read_csv('data/jobs_incoming.csv')

    if df.empty:
        print("No data in incoming file")
        return

    # remove duplicates
    existing_ids = pd.read_sql("SELECT job_id FROM jobs", conn)

    if not existing_ids.empty:
        df = df[~df['job_id'].isin(existing_ids['job_id'])]

    if df.empty:
        print("No new data to add")
        return

    # get last ingestion time
    last_date_df = pd.read_sql(
        "SELECT MAX(ingestion_timestamp) as last_date FROM jobs",
        conn
    )

    if last_date_df["last_date"][0] is None:
        ingestion_time = datetime.now()
    else:
        last_date = pd.to_datetime(last_date_df["last_date"][0])
        gap_days = random.choice([1,2,3,4,5])
        ingestion_time = last_date + timedelta(days=gap_days)

    df['ingestion_timestamp'] = ingestion_time

    # insert into DB
    df.to_sql("jobs", conn, if_exists="append", index=False)

    print(f"{len(df)} new rows inserted on {ingestion_time}")

    
