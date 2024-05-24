# data/data_fetcher.py
import psycopg2
import pandas as pd
from config import DATABASE_CONFIG

def fetch_data(query):
    conn = psycopg2.connect(**DATABASE_CONFIG)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df