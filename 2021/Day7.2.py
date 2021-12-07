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

def calcSum(n):
    return n * (n + 1) / 2

while not(found):
    a = b = c = 0
    for n in range(0, len(crabs)):
        a += calcSum(abs(pos - 1 - crabs[n]))
        b += calcSum(abs(pos - crabs[n]))
        c += calcSum(abs(pos + 1 - crabs[n]))
    if a > b and b < c:
        found = True
    elif a < b and b < c:
        pos -= 1
    else:
        pos += 1
print(b)