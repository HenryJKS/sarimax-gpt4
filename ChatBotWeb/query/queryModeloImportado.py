from ChatBotWeb.databaseconnection import connection

df = connection.mysql_query('''SELECT IMPORTADO as Importado, MODELO as Modelo, ANO as Ano FROM VEICULO_IMPORTADO''')
