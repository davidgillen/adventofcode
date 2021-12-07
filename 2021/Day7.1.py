#fp = open('Input7.sample')
fp = open('Input7.txt')

crabs = []
total = 0

for crab in fp.readline().split(','):
    crabs.append(int(crab))
    total += int(crab)

pos = 4
found = False
minPos = 0
minVal = 999999999

# Brute force
for pos in range(0, len(crabs)):
    val = 0
    for n in range(0, len(crabs)):
        val += abs(pos - crabs[n])
    if val < minVal:
        minPos = pos
        minVal = val

print(minPos)

fuel = 0
for n in range(0, len(crabs)):
    fuel += abs(minPos - crabs[n])
print(fuel)

# Stop when found
while not(found):
    a = b = c = 0
    for n in range(0, len(crabs)):
        a += abs(pos - 1 - crabs[n])
        b += abs(pos - crabs[n])
        c += abs(pos + 1 - crabs[n])
    if a > b and b < c:
        found = True
    elif a < b and b < c:
        pos -= 1
    else:
        pos += 1

fuel = 0
for n in range(0, len(crabs)):
    fuel += abs(minPos - crabs[n])
print(fuel)