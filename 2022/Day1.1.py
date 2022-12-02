fp = open('input1.txt')
#fp = open('test1.txt')
lines = fp.readlines()

fatty = 0
currentTotal = 0
for line in lines:
    if line == '\n':
        if currentTotal > fatty:
            fatty = currentTotal
        currentTotal = 0
    else:
        currentTotal += int(line[:-1])

if currentTotal > fatty:
    fatty = currentTotal
print(fatty)