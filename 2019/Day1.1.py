import math
fp = open('Day1.input')
lines = fp.readlines()

total = 0
for line in lines:
    total = total + math.floor(int(line) / 3 ) - 2

print(total)