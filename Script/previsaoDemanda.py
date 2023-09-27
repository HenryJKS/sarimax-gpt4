import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

pd.set_option('display.max_columns', None)

# Usar SARIMAX para prever a demanda de veículos elétricos
# SARIMAX é uma extensão do modelo ARIMA para dados não sazonais
# ARIMA - AutoRegressive Integrated Moving Average

df = pd.read_csv('C:\\Users\\logonrmlocal\\Desktop\\dados.csv', sep=',', index_col='ANO')

# usar random forest para prever a demanda de veículos elétricos
# random forest é um algoritmo de aprendizado supervisionado

# plotar gráfico de linha para visualizar a demanda de veículos elétricos
df['UNIDADES_VENDIDAS'].plot(figsize=(12, 5), title='Demanda de veículos elétricos', fontsize=14)
plt.show()


# prever UNIDADES_VENDIDAS para 2023
# usar random forest para prever a demanda de veículos elétricos
# random forest é um algoritmo de aprendizado supervisionado
