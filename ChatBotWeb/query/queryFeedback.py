from ChatBotWeb.databaseconnection.connection import mysql_query

query = '''SELECT * FROM FEEDBACK_CLIENTE'''

data = mysql_query(query)


