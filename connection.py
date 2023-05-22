import os
import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='Bookshop',
    user='postgres',
    password='postgres'
)
