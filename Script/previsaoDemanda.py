import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from statsmodels.tsa.arima.model import ARIMA

from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from ChatBotWeb.query.queryPrevisaoDemanda import df

pd.set_option('display.max_columns', None)

# Usar SARIMAX para prever a demanda de veículos elétricos
# SARIMAX é uma extensão do modelo ARIMA para dados não sazonais
# ARIMA - AutoRegressive Integrated Moving Average

