import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.statespace.sarimax import SARIMAX
pd.set_option('display.max_columns', None)
from ChatBotWeb.query.queryPrevisaoDemanda import df

pd.set_option('display.max_columns', None)

df = df.drop(columns=['CARRO_MODELO', 'MODELO_ESTOQUE'])

df = pd.get_dummies(df, columns=['TENDENCIA_MERCADO', 'INDICADOR_ECONOMICO', 'ATIVIDADE_CONCORRENTE', 'EPOCA_ANO',
                                 'PROMOCAO'])
df = df * 1

# Separando os dados em treino e teste
X = df.drop(columns=['NUMEROS_VENDAS'])
y = df['NUMEROS_VENDAS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Ajustar hipermarametros
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': [1.0, 'sqrt', 'log2']
}

rf = RandomForestRegressor()

grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
print(grid_search.best_score_)



