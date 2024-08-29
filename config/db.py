#!/usr/bin/env python3
import psycopg2
import functools
import os
from dotenv import load_dotenv
from os import environ
load_dotenv()


def connection_db(func):
    '''Decorator to connect to the database'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        cur = conn.cursor()
        kwargs['cur'] = cur
        kwargs['conn'] = conn
        result = func(*args, **kwargs)
        conn.commit()
        cur.close()
        conn.close()
        return result
    return wrapper
