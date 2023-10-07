from ChatBotWeb.databaseconnection import connection

df = connection.mysql_query('''SELECT IMPORTADO as Unidades_Importada, MODELO as Modelo, ANO as Ano FROM VEICULO_IMPORTADO''')

