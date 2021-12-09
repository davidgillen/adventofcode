fp = open('Input9.txt')
#fp = open('Input9.sample')

heights = {}
lines = fp.readlines()
for x in range(0, len(lines)):
    for y in range(0, len(lines[0])-1):
        heights[(x,y)] = lines[x][y]


def checkLowPoint(x, y):
    global heights
    if (x-1, y) in heights.keys() and heights[(x-1, y)] <= heights[(x, y)]:
        return 0
    if (x+1, y) in heights.keys() and heights[(x+1, y)] <= heights[(x, y)]:
        return 0
    if (x, y-1) in heights.keys() and heights[(x, y-1)] <= heights[(x, y)]:
        return 0
    if (x, y+1) in heights.keys() and heights[(x, y+1)] <= heights[(x, y)]:
        return 0
    print(heights[(x,y)])
    return int(heights[(x, y)]) + 1

total = 0
for x in range(0, len(lines)):
    for y in range(0, len(lines[0])-1):
        low = checkLowPoint(x, y)
        if low > 0:
            total += low


print(total)
            