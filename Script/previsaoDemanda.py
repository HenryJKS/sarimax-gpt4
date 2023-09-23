import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from ChatBotWeb.query.queryPrevisaoDemanda import df

# Transformando a coluna de data em datetime
df['DATA_VENDA'] = pd.to_datetime(df['DATA_VENDA'])

# formatando DATA_VENDA para previsão de NUMERO_VENDAS por mes
df['MES'] = df['DATA_VENDA'].dt.month
df['ANO'] = df['DATA_VENDA'].dt.year

# Excluir coluna de data
df = df.drop(columns=['DATA_VENDA'])

# Codificação one-hot para TENDENCIA_MERCADO, INDICADOR_ECONOMICO, ATIVIADE_CONCORRENTE, PROMOTIONS
df = pd.get_dummies(df, columns=['CARRO_MODELO', 'TENDENCIA_MERCADO', 'INDICADOR_ECONOMICO', 'ATIVIDADE_CONCORRENTE', 'EPOCA_ANO', 'PROMOCAO'])

# Criar modelo para prever NUMERO_VENDAS por mes
X = df.drop(columns=['NUMEROS_VENDAS'])
y = df['NUMEROS_VENDAS']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Prever os dados de teste
y_pred = modelo.predict(X_test)

# Calcular o erro médio quadrático
mse = np.mean((y_pred - y_test) ** 2)
print('Erro médio quadrático: ', mse)

# Calcular o coeficiente de determinação
r2 = modelo.score(X_test, y_test)
print('Coeficiente de determinação: ', r2)
