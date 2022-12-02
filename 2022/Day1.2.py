fp = open('input1.txt')
#fp = open('test1.txt')
lines = fp.readlines()

fatty1 = fatty2 = fatty3 = 0
currentTotal = 0
for line in lines:
    if line == '\n':
        if currentTotal > fatty1:
            fatty3 = fatty2
            fatty2 = fatty1
            fatty1 = currentTotal
        elif currentTotal > fatty2:
            fatty3 = fatty2
            fatty2 = currentTotal
        elif currentTotal > fatty3:
            fatty3 = currentTotal
        currentTotal = 0
    else:
        currentTotal += int(line[:-1])

if currentTotal > fatty1:
    fatty3 = fatty2
    fatty2 = fatty1
    fatty1 = currentTotal
elif currentTotal > fatty2:
    fatty3 = fatty2
    fatty2 = currentTotal
elif currentTotal > fatty3:
    fatty3 = currentTotal
print(fatty1 + fatty2 + fatty3)