#fp = open('Input5.sample')
fp = open('Input5.txt')

vents = {}
for line in fp.readlines():
    start, end = line.strip().split(' -> ')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x1 == x2:
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp
        for y in range(y1,y2+1):
            if (x1, y) in vents:
                vents[(x1,y)] += 1
            else:
                vents[(x1,y)] = 1
    elif y1 == y2:
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
        for x in range(x1, x2+1):
            if (x, y1) in vents:
                vents[(x, y1)] += 1
            else:
                vents[(x, y1)] = 1
    else:
        if x1 > x2:
            xRange = list(reversed(range(x2, x1+1)))
        else:
            xRange = range(x1, x2+1)
        if y1 > y2:
            yRange = list(reversed(range(y2, y1+1)))
        else:
            yRange = range(y1, y2+1)
        
        for n in range(0,len(xRange)):
            if (xRange[n], yRange[n]) in vents:
                vents[(xRange[n], yRange[n])] += 1
            else:
                vents[(xRange[n], yRange[n])] = 1
        


count = 0
for key, vent in vents.items():
    if vent >= 2:
        count += 1
print(count)