import math
fp = open('Day1.input')
lines = fp.readlines()

def calcFuel(mass):
    newMass = math.floor(mass / 3) - 2
    if newMass <= 0:
        return 0
    else:
        return newMass + calcFuel(newMass)

total = 0
for line in lines:
    total = total + calcFuel(int(line))
print(total)