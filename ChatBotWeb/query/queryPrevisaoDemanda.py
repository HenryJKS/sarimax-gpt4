from ChatBotWeb.databaseconnection.connection import mysql_query
import pandas as pd
pd.set_option('display.max_columns', None)

query_2019='''SELECT MARCA, UNIDADES_VENDIDAS, AUTONOMIA, MARCA_CONHECIDA, INCENTIVOS_FISCAIS, ACESSIVEL, ANO 
FROM CARROS_ELETRICO WHERE ANO = 2019'''

query_2020='''SELECT MARCA, UNIDADES_VENDIDAS, AUTONOMIA, MARCA_CONHECIDA, INCENTIVOS_FISCAIS, ACESSIVEL, ANO
FROM CARROS_ELETRICO WHERE ANO = 2020'''

query_2021='''SELECT MARCA, UNIDADES_VENDIDAS, AUTONOMIA, MARCA_CONHECIDA, INCENTIVOS_FISCAIS, ACESSIVEL, ANO
FROM CARROS_ELETRICO WHERE ANO = 2021'''

query_2022='''SELECT MARCA, UNIDADES_VENDIDAS, AUTONOMIA, MARCA_CONHECIDA, INCENTIVOS_FISCAIS, ACESSIVEL, ANO
FROM CARROS_ELETRICO WHERE ANO = 2022'''


df_2019 = mysql_query(query_2019)
df_2020 = mysql_query(query_2020)
df_2021 = mysql_query(query_2021)
df_2022 = mysql_query(query_2022)

#pivoter a coluna AUTONOMIA
df_2019 = df_2019.pivot_table(index=['MARCA', 'UNIDADES_VENDIDAS', 'MARCA_CONHECIDA', 'INCENTIVOS_FISCAIS', 'ACESSIVEL', 'ANO'], columns='AUTONOMIA', aggfunc='size', fill_value=0)
df_2020 = df_2020.pivot_table(index=['MARCA', 'UNIDADES_VENDIDAS', 'MARCA_CONHECIDA', 'INCENTIVOS_FISCAIS', 'ACESSIVEL', 'ANO'], columns='AUTONOMIA', aggfunc='size', fill_value=0)
df_2021 = df_2021.pivot_table(index=['MARCA', 'UNIDADES_VENDIDAS', 'MARCA_CONHECIDA', 'INCENTIVOS_FISCAIS', 'ACESSIVEL', 'ANO'], columns='AUTONOMIA', aggfunc='size', fill_value=0)
df_2022 = df_2022.pivot_table(index=['MARCA', 'UNIDADES_VENDIDAS', 'MARCA_CONHECIDA', 'INCENTIVOS_FISCAIS', 'ACESSIVEL', 'ANO'], columns='AUTONOMIA', aggfunc='size', fill_value=0)

# resetar o index
df_2019 = df_2019.reset_index()
df_2020 = df_2020.reset_index()
df_2021 = df_2021.reset_index()
df_2022 = df_2022.reset_index()


# Juntar as tabelas
df = pd.concat([df_2019, df_2020, df_2021, df_2022], ignore_index=True)
# o ano é o index
df = df.set_index('ANO')

# renomear coluna ALTA, BAIXA, MEDIA para AUTONOMIA_ALTA, AUTONOMIA_BAIXA, AUTONOMIA_MEDIA
df = df.rename(columns={'Alta': 'AUTONOMIA_ALTA', 'Baixa': 'AUTONOMIA_BAIXA', 'Media': 'AUTONOMIA_MEDIA'})
