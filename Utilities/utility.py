import pymssql
import psycopg2
from flask import Flask, request, make_response
import os,json

def func():
    print("Hello from utility")

#for MSSQL DB connections
def connect_sql_db():
    try:
        db_name = ""
        user = ""
        password = ""
        host = ""

        connection = pymssql.connect(server=host, user=user,password=password, database=db_name)
        return connection
    except Exception as e:
        print("DB connection error")
        print(e)
        return None

#for Postgress DB connections
def connect_postgress_db():
    try:
        dbname = ""
        user = ""
        password = ""
        host = ""
        port= "9432"

        connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
        )
        print("Connected to the database")
        return connection
    except:
        print("DB connection error")
        return None
