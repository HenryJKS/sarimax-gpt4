import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

# Usar SARIMAX para prever a demanda de veículos elétricos
# SARIMAX é uma extensão do modelo ARIMA para dados não sazonais
# ARIMA - AutoRegressive Integrated Moving Average

df = pd.read_csv('C:\\Users\\Henry\\Desktop\\ProjectChallenge\\ChatBotWeb\\assets\\dados.csv', sep=',', index_col='ANO')
df = df.drop('MARCA', axis=1)

endog = df['UNIDADES_VENDIDAS']
exog = df.drop('UNIDADES_VENDIDAS', axis=1)

# Ajustar o modelo SARIMAX
modelo = sm.tsa.statespace.SARIMAX(endog, exog, order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
resultado = modelo.fit()

# Prever a demanda para os próximos 2 anos
previsao = resultado.get_forecast(steps=2, exog=exog.iloc[-2:])

# criar um dataframe com os valores previstos
df_previsao = previsao.summary_frame(alpha=0.05)

# armazenar media, erro padrão, intervalo de confiança inferior e superior em variáveis
media = df_previsao['mean'].tolist()
erro_padrao = df_previsao['mean_se'].tolist()
intervalo_confianca_inferior = df_previsao['mean_ci_lower'].tolist()
intervalo_confianca_superior = df_previsao['mean_ci_upper'].tolist()

df_previsao = df_previsao.drop(['mean_se', 'mean_ci_lower', 'mean_ci_upper'], axis=1)

VENDAS_PREVISAO = df_previsao['mean'].values.tolist()
VENDAS_PREVISAO = [round(num) for num in VENDAS_PREVISAO]

df_previsao = pd.DataFrame({'ANO': [2023, 2024], 'UNIDADES_VENDIDAS': VENDAS_PREVISAO})
