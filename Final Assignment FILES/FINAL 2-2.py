import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

data = pd.read_csv("Final Assignment FILES\spacex.csv")

'''Showing data details to help in further operations'''

data.head(10)
print(data.shape)
print(data.info())
print(data.describe())

'''Using some graphs to have original data information'''

sns.lineplot(data=data, x="Datetime", y="Volume")
plt.xticks(rotation=45)
plt.title("Trading Volume")
plt.show()

sns.histplot(data["Close"], bins=30)
plt.title("Close Price Distribution")
plt.show()

sns.boxplot(data=data["Close"])
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="Blues")
plt.show()

production = data["Close"].values.reshape(-1,1)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(production)

window_size = 20


'''Predictions Process    
TRYING TO PREDICT CLOSING PRICE (Took some help in Dropout part)'''
X = []
y = []

for i in range(window_size, len(scaled_data)):
    X.append(scaled_data[i-window_size:i,0])
    y.append(scaled_data[i,0])

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,shuffle=False)

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

model = Sequential()

model.add(LSTM(128,return_sequences=True,input_shape=(X_train.shape[1],1)))

model.add(Dropout(0.2))

model.add(LSTM(128))

model.add(Dropout(0.2))

model.add(Dense(1))

model.compile(optimizer="adam",loss="mean_squared_error")

history = model.fit(X_train,y_train,epochs=20,batch_size=32,validation_split=0.1)

predictions = model.predict(X_test)

predictions = scaler.inverse_transform(predictions)

y_test = scaler.inverse_transform(y_test.reshape(-1,1))

plt.figure(figsize=(12,6))

plt.plot(y_test, label="Actual")
plt.plot(predictions, label="Predicted")

plt.legend()

plt.show()

"""PROCESS FAILED"""

'''PREDICTING WITH LINEAR REGRESSION'''


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


print(data.head())
print(data.shape)
print(data.info())
print(data.describe())


sns.pairplot(data)

plt.show()


features = ["Open", "High", "Low", "Volume"]

X = data[features]

y = data["Close"]

"""Splitting Data to have a Original Values and some values to predict(TOOK AI help in this part)
"""
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=42)


model = LinearRegression()

"""Training"""

history = model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error :", mae)
print("Mean Squared Error :", mse)
print("Root Mean Squared Error :", rmse)
print("R2 Score :", r2)

"""Showing The results"""

plt.figure(figsize=(12,6))
plt.plot(y_test.values,label="Actual Price")
plt.plot(predictions,label="Predicted Price")
plt.title("Actual vs Predicted Close Price")
plt.xlabel("Samples")
plt.ylabel("Close Price")
plt.legend()
plt.show()

"""Scatter Plot to Show the Original and Predicted Values"""

plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test,y=predictions)
plt.xlabel("Actual Close Price")
plt.ylabel("Predicted Close Price")
plt.title("Linear Regression Prediction")
plt.show()

"""Showing Coefficient"""

coef = pd.DataFrame(model.coef_,features,columns=["Coefficient"])

print(coef)
print("Intercept :", model.intercept_)