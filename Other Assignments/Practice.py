Costumerinfo="Tim Kate is a prime costumer of ABC Inc. He lives in California"
print(Costumerinfo)
print(type(Costumerinfo))

print(len(Costumerinfo))

print(Costumerinfo[32:35:1])

for c in Costumerinfo:
    print(c)



CostumerList=["Tim Kate", 54 , 6.12 , "ABC Inc", True]

print(CostumerList[1])
print(CostumerList[3])

print(type(CostumerList[1]))
print(type(CostumerList[3]))    

CostumerList.append(30000)

print(CostumerList)

CostumerList.insert(1, "Lahore")

print(CostumerList)

CostumerList.remove(54)

CostumerList.pop(0)

print(CostumerList)

print(len(CostumerList))

for x in CostumerList:
    print(x)

CostumerList[0]="Change Value"

print(CostumerList)

CostumerTuples = ("Tim Kate", 54 , 6.12 , "ABC Inc", True)

print(CostumerTuples[0])
print(CostumerTuples[3])

print(type(CostumerTuples[0]))

#CostumerTuples [0] = "New Value"   #TO LEARN

CostumerSet = {"Tim Kate", 54 , 6.12 , "ABC Inc", True}

print(CostumerSet)
print(type(CostumerSet))
print(len(CostumerSet))

for y in CostumerSet:
    print(y)

CostumerSet.add("Lahore")

print(CostumerSet)

costumerdictionary = {"Name":"Tim Kate","Age": 54 , "Height" : 6.12 , "Company":"ABC Inc","Status": True}

print(costumerdictionary)
print(type(costumerdictionary))

costumerdictionary["Name"] = "Tom Kate"

print(costumerdictionary)

costumerdictionary["University"] = "Harvard"

print(costumerdictionary)

for x in costumerdictionary:
    print(x)

for x in costumerdictionary:
    print(costumerdictionary[x])