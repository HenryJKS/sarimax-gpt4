from ChatBotWeb.databaseconnection.connection import mysql_query

query = '''SELECT CARRO_MODELO, YEAR(DATA_VENDA) AS ANO, MONTH(DATA_VENDA) AS MES, NUMEROS_VENDAS, MODELO_ESTOQUE, TENDENCIA_MERCADO, 
INDICADOR_ECONOMICO, ATIVIDADE_CONCORRENTE, EPOCA_ANO, PROMOCAO FROM demandforecasting
'''

query1 = '''SELECT DATA_VENDA, NUMEROS_VENDAS FROM demandforecasting
ORDER BY 1 DESC
'''

df = mysql_query(query1)
