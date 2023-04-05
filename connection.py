import os
import psycopg2

connection = psycopg2.connect(
    host=os.environ.get('HOST'),
    database=os.environ.get('DATABASE'),
    user=os.environ.get('USER'),
    password=os.environ.get('PASSWORD')
)
