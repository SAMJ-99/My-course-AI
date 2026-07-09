#Usa Realstate File

import numpy as npy

price, bed, bath, size = npy.genfromtxt('FULL-STACK-B-8-Wed-Thru-Fri\Week4\RealEstate-USA.csv', delimiter=',', usecols=(2,3,4,10), unpack=True, dtype=None,skip_header=1)

print(price)
print(bed)
print(bath)
print(size)