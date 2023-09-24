import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from ChatBotWeb.query.queryPrevisaoDemanda import df
pd.set_option('display.max_columns', None)
from pandas.tseries.offsets import DateOffset
df.index = pd.to_datetime(df['DATA_VENDA'])
df = df.sort_index(ascending=True, axis=0)
df = df.drop(columns=['DATA_VENDA'])

# decompose_data = seasonal_decompose(df, model="additive")
# decompose_data.plot()
# plt.show()
#
# seasonality=decompose_data.seasonal
# seasonality.plot(color='green')
# plt.show()

from statsmodels.tsa.stattools import adfuller
dftest = adfuller(df.NUMEROS_VENDAS, autolag = 'AIC')
print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
    print("\t",key, ": ", val)

rolling_mean = df.rolling(window = 12).mean()
df['rolling_mean_diff'] = rolling_mean - rolling_mean.shift()
ax1 = plt.subplot()
df['rolling_mean_diff'].plot(title='after rolling mean & differencing');
ax2 = plt.subplot()
df.plot(title='original')


dftest = adfuller(df['rolling_mean_diff'].dropna(), autolag = 'AIC')
print("1. ADF : ",dftest[0])
print("2. P-Value : ", dftest[1])
print("3. Num Of Lags : ", dftest[2])
print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
print("5. Critical Values :")
for key, val in dftest[4].items():
  print("\t",key, ": ", val)


model = sm.tsa.statespace.SARIMAX(df['NUMEROS_VENDAS'], order=(1,1,1), seasonal_order=(1,1,1,12))
results = model.fit()

df['forecast'] = results.predict(start = 90, end= 103, dynamic= True)
df[['NUMEROS_VENDAS', 'forecast']].plot(figsize=(12, 8))
plt.show()

pred_date=[df.index[-1]+ DateOffset(months=x)for x in range(0,24)]

prepared_df=pd.DataFrame(index=pred_date[1:],columns=df.columns)

df = pd.concat([df,prepared_df])

df['forecast'] = results.predict(start = 104, end = 120, dynamic= True)
df[['NUMEROS_VENDAS', 'forecast']].plot(figsize=(12, 8))
plt.show()