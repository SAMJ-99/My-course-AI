"""
Rocket Lab Analytics Budget Vs Employees
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

"""Loading Data"""

data = pd.read_csv("Final Assignment FILES\RocketLab_Analytics_2010_2024.csv")

print(data.head())
print(data.shape)
print(data.info())
print(data.describe())

"""Budget and Employee Analysis"""

plt.figure(figsize=(12,6))
sns.lineplot(data=data,x="Year",y="Budget_Funding_USD_M",marker="o")
plt.title("Budget Growth")
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=data,x="Year",y="Employees",marker="o")
plt.title("Employee Growth")
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=data,x="Budget_Funding_USD_M",y="Employees",s=120)
plt.title("Budget vs Employees")
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(data["Budget_Funding_USD_M"],bins=10,kde=True)
plt.title("Budget Distribution")
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(data["Employees"],bins=10,kde=True)
plt.title("Employee Distribution")
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(data.corr(numeric_only=True),annot=True,cmap="Blues")
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(data)
plt.show()

print("Highest Budget")
print(data.loc[data["Budget_Funding_USD_M"].idxmax()])

print("Lowest Budget")
print(data.loc[data["Budget_Funding_USD_M"].idxmin()])

print("Highest Employees")
print(data.loc[data["Employees"].idxmax()])

print("Lowest Employees")
print(data.loc[data["Employees"].idxmin()])

data["Budget_per_Employee"] = data["Budget_Funding_USD_M"]/data["Employees"]

plt.figure(figsize=(12,6))
sns.lineplot(data=data,x="Year",y="Budget_per_Employee",marker="o")
plt.title("Budget per Employee")
plt.show()

"""LSTM Model
Predict next year's Budget using previous 3 years."""

production = data["Budget_Funding_USD_M"].values.reshape(-1,1)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(production)

window_size = 3

X=[]
y=[]

for i in range(window_size,len(scaled_data)):
    X.append(scaled_data[i-window_size:i,0])
    y.append(scaled_data[i,0])

X=np.array(X)
y=np.array(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)

X_train=X_train.reshape((X_train.shape[0],X_train.shape[1],1))
X_test=X_test.reshape((X_test.shape[0],X_test.shape[1],1))

model=Sequential()

model.add(LSTM(64,return_sequences=True,input_shape=(X_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(64))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(optimizer="adam",loss="mean_squared_error")

history=model.fit(X_train,y_train,epochs=30,batch_size=4,validation_split=0.1)

predictions=model.predict(X_test)

predictions=scaler.inverse_transform(predictions)

y_test=scaler.inverse_transform(y_test.reshape(-1,1))

plt.figure(figsize=(12,6))
plt.plot(y_test,label="Actual Budget")
plt.plot(predictions,label="Predicted Budget")
plt.title("Actual vs Predicted Budget")
plt.legend()
plt.show()





"""As we have a few values, 15 to be exact, 
the LSTM Cant Have sufficient samples to make good prediction"""



