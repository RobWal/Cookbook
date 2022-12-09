import os
import psycopg2
from psycopg2.extras import DictCursor

conn_string = os.environ.get("DATABASE_URL")

def sql_select(query, params):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute(query, params)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def sql_write(query, params):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()
