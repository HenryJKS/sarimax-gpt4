import mysql.connector as mysql
import pandas as pd
from ChatBotWeb.databaseconnection import connection

df = connection.mysql_query('''SELECT YEAR(DATA_FATURAMENTO) AS Ano, SUM(VALOR_FATURAMENTO) AS Faturamento
                                FROM FATURAMENTO
                                GROUP BY 1
                                ORDER BY 1''')
