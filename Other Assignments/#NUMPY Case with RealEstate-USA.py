#NUMPY Case with RealEstate-USA

import numpy as np

price, city, size = np.genfromtxt('RealEstate-USA.csv', delimiter=',', usecols=(2,7,10), unpack=True, dtype=None, skip_header=1)

#Printing Values
print(price)
print(city)
print(size)

#checking average values of all properties
print("USA Realestate average price:" , np.average(price))
print("These properties average size is:" , np.average(size))

#checking Max values of all properties
print("USA Realestate Max price:" , np.max(price))
print("These properties Max size is:" , np.max(size))

#checking Min values of all properties
print("USA Realestate Min price:" , np.min(price))
print("These properties Min size is:" , np.min(size))

#checking Total values of all properties
print("The total Value of all these properties is:" , np.sum(price))
print("The total area of our properties is :" , np.sum(size))

print()