#Importing all required tools
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Showing values using Numpy
mpg, cyl, hp, wg, yr = np.genfromtxt('Automobile.csv', delimiter=',', usecols=(1,2,4,5,7), unpack=True, dtype=None,skip_header=1)

print(mpg)
print(cyl)
print(hp)
print(wg)
print(yr)

#Creating dataframe with pandas
df = pd.read_csv('Automobile.csv', delimiter=",")

print(df)

'''Dividing our Dataframe in 2 parts, first one up to 4 cylinders so we can see the mileage curve'''

df_upto4 = df.query('cylinders <=4')

print(df_upto4)

#Using seaborn to create the graph
sns.set_theme(style='dark')
sns.lineplot(x='cylinders', y='mpg', data=df_upto4)
plt.show()

print ()

#As most of our data is numerical trying to use regression
newdf = df_upto4[["cylinders", "mpg"]]
print(newdf)

newdf.plot.scatter(x='cylinders', y='mpg', title= 'Scatter Plot of Nmbers of Cylinder and consumption' )
plt.show()

print("newdf.shape:         " , newdf.shape)

y = newdf['cylinders'].values.reshape(-1,1)
x = newdf['mpg'].values.reshape(-1,1)

print("y :  " , y)
print("x :   " , x)

print(x.shape)

SEED = 35
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = SEED)

print(y_train)
print(x_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(x_train, y_train)

print(regressor.coef_)

def calc(slope, intercept, cylinders):
    return slope*cylinders+intercept
print()

#Predicting our number of cylinders giving mpg(Miles per gallon)

Cylinders = calc(regressor.coef_, regressor.intercept_, 4)
print(Cylinders)

Cylinders = regressor.predict([[4]])
print(Cylinders)

y_pred = regressor.predict(x_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)



'''Dividing our Dataframe in 2 parts, Second one is <4 to 8 cylinders so we can see the mileage decreasing'''

df_greater4 = df.query('cylinders >=4')

print(df_greater4)

#Using seaborn to create the graph
sns.set_theme(style='dark')
sns.lineplot(x='cylinders', y='mpg', data=df_greater4)
plt.show()

print ()

#As most of our data is numerical trying to use regression
newdf1 = df_greater4[["cylinders", "mpg"]]
print(newdf1)

newdf1.plot.scatter(x='cylinders', y='mpg', title= 'Scatter Plot of Nmbers of Cylinder and consumption' )
plt.show()

print("newdf1.shape:         " , newdf1.shape)

y1 = newdf1['cylinders'].values.reshape(-1,1)
x1 = newdf1['mpg'].values.reshape(-1,1)

print("y1 :  " , y1)
print("x1 :   " , x1)

print(x1.shape)

SEED = 35
from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size = 0.2, random_state = SEED)

print(y1_train)
print(x1_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(x1_train, y1_train)

print(regressor.coef_)

def calc(slope, intercept, cylinders):
    return slope*cylinders+intercept
print()

#Predicting our number of cylinders giving mpg(Miles per gallon)

Cylinders = calc(regressor.coef_, regressor.intercept_, 8)
print(Cylinders)

Cylinders = regressor.predict([[8]])
print(Cylinders)

y1_pred = regressor.predict(x1_test)

df_preds1 = pd.DataFrame({'Actual': y1_test.squeeze(), 'Predicted': y1_pred.squeeze()})
print(df_preds1)

print()