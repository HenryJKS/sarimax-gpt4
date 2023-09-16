import os

import pandas as pd
import mysql.connector as mysql

from dotenv import load_dotenv
load_dotenv()

DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')


def mysql_query(query):
    db_params = {
        'database': DATABASE,
        'user': USER,
        'password': PASSWORD,
        'host': HOST
    }

    connection = mysql.connect(**db_params)
    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(result, columns=column_names, index=None)

    cursor.close()
    connection.close()

    return df
