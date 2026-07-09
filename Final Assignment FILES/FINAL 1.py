import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Inserting values using Numpy with CSV
Launches, successful, Failed, Budget, Successrate = np.genfromtxt('Final Assignment FILES\Space_Industry_Analytics_2010_2024.csv', delimiter=',', usecols=(2,3,4,6,9), unpack=True, dtype=None,skip_header=1)

print("All data is from 2010 to 2024")
#Budget stats

print("Total Budget Used: ", np.sum(Budget), "Million USD")
print("Average Budget: ", np.mean(Budget))
print("Maximum Budget: ", np.max(Budget))
print("Minimum Budget: ", np.min(Budget))

#Launches Stats
print("Total Launches: ", np.sum(Launches))
print("Average Launches Per Year: ", np.mean(Launches))
print("Maximum Launches: ", np.max(Launches))
print("Minimum Launches: ", np.min(Launches))

#Success Rate
print("Average Success Rate: ", np.mean(Successrate), "%")
print("Highest Success Rate: ", np.max(Successrate), "%")
print("Lowest Success Rate: ", np.min(Successrate), "%")

#Performing some Pandas operation

space = pd.read_csv("Space_Industry_Analytics_2010_2024.csv")

# Dividing data by company using loc
spacex = space.loc[space["Company"] == "SpaceX"]
nasa = space.loc[space["Company"] == "NASA"]
rocketlab = space.loc[space["Company"] == "Rocket Lab"]

# SpaceX data with iloc

SpaceXloc = space.iloc[1:15]

print(SpaceXloc)

#Nasa data with iloc

Nasaloc = space.iloc[15:30]
print(Nasaloc)

#Rocket Lab data with iloc

Rocket = space.iloc[30:]
print(Rocket)

#Seaborn Operations
#Total Launches
sns.barplot(data=space, x="Company", y="Launches")

plt.title("Launches by Company")
plt.xlabel("Company")
plt.ylabel("Number of Launches")

plt.show()

#Company Budget

sns.barplot(data=space, x="Company", y="Budget_Funding_USD_M")

plt.title("Budget by Company")
plt.xlabel("Company")
plt.ylabel("Budget (Million USD)")

plt.show()

sns.scatterplot(data=space,x="Budget_Funding_USD_M",y="Launches",hue="Company",s=100)

plt.title("Budget vs Launches")
plt.xlabel("Budget (Million USD)")
plt.ylabel("Launches")

plt.show()