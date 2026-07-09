import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

spacex = pd.read_csv("Final Assignment FILES\spacex.csv")
#Variables

open_price = spacex["Open"]
close_price = spacex["Close"]
high_price = spacex["High"]
low_price = spacex["Low"]
volume = spacex["Volume"]

#Showing Values

print("<<<<<<<< Volume Statistics >>>>>>>>")

print("Highest Volume: ", np.max(volume))
print("Lowest Volume: ", np.min(volume))
print("Average Volume: ", np.mean(volume))
print("Median Volume: ", np.median(volume))
print("Volume Standard Deviation: ", np.std(volume))

#Percentile

print("25th Percentile Volume: ", np.percentile(volume, 25))
print("50th Percentile Volume: ", np.percentile(volume, 50))
print("75th Percentile Volume: ", np.percentile(volume, 75))


#Other operation combining math with pandas

print("Price Difference (High - Low):")
print(high_price - low_price)

print("Average Trading Price:")
average_price = (open_price + close_price) / 2
print(average_price)

print("Price Range:")
price_range = np.max(high_price) - np.min(low_price)
print(price_range)

print("Total Volume Traded:")
print(np.sum(volume))

#Stock Prices by Time

sns.lineplot(data=spacex, x="Datetime", y="Close")

plt.title("SpaceX Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.xticks(rotation=45)
plt.show()

correlation = spacex[["Open", "High", "Low", "Close", "Volume"]].corr()

sns.heatmap(correlation,annot=True, cmap="coolwarm")

plt.title("Correlation Matrix")

plt.show()