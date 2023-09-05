from ChatBotWeb.databaseconnection import connection

df = connection.mysql_query('''SELECT VE.MODELO AS MODELO, VEP.TIPO_PROBLEMA AS PROBLEMA FROM VEICULO VE 
JOIN VEICULO_PROBLEMA VEP
ON VE.ID_VEICULO = VEP.ID_VEICULO''')
