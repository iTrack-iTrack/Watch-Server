import os
import sqlite3

def initialise():
    connection = sqlite3.connect(os.getenv("DB_PATH"), check_same_thread=False)
    cursor     = connection.cursor()
    return connection, cursor

def terminate(connection, cursor):
    connection.close()
