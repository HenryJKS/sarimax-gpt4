from ChatBotWeb.databaseconnection.connection import mysql_query

query = '''SELECT * FROM DEMANDFORECASTING'''

df = mysql_query(query)

df = df.drop(columns=['ID'])
