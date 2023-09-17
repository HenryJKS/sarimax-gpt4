import mysql.connector as mysql
import pandas as pd
from ChatBotWeb.databaseconnection import connection

df = connection.mysql_query('''SELECT YEAR(DATA) AS Ano, VE.MODELO As Modelo, ROUND(SUM(VALOR),2) AS Faturamento FROM FATURAMENTO_VEICULO FE
JOIN VEICULO VE
ON VE.ID_VEICULO = FE.ID_VEICULO
GROUP BY 1, 2
ORDER BY 2, 1''')
