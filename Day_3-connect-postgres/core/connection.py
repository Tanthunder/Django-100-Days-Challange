''' connecting to postgres db '''

import psycopg2
import os

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="day3_djangopostgres",
    user=os.environ.get('POSTGRES_DB_USER'),
    password=os.environ.get('POSTGRES_DB_PAS'),
)
conn.autocommit = True

cursor = conn.cursor()