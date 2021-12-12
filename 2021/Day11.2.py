#fp = open('Input11.sample')
fp = open('Input11.txt')

grid = {}
row = 0
position = 0
for line in fp.readlines():
    for position in range(0, len(line.strip())):
        grid[(position, row)] = int(line[position])
    row += 1


def flashIncrement(x ,y):
    global grid
    for m in range(-1, 2):
        for n in range(-1, 2):
            if (x+m, y+n) in grid:
                grid[(x+m, y+n)] += 1

totalFlashes = 0
print(position)
print(row)
synced = False
iterations = 0
while not synced:
    iterations += 1
    totalFlashes = 0
    # Increment everything
    for x in range(0, position+1):
        for y in range(0, row):
            grid[(x, y)] += 1

    flashes = True
    flashed = []
    while flashes:
        flashes = False
        for x in range(0, (position+1)):
            for y in range(0, row):
                if grid[(x,y)] > 9 and (x,y) not in flashed:
                    flashes = True
                    flashed.append((x,y))
                    flashIncrement(x, y)
                    totalFlashes += 1
    
    if totalFlashes == 100:
        synced = True

    for x in range(0, position+1):
        for y in range(0, row):
            if grid[(x,y)] > 9:
                grid[(x,y)] = 0
        
print(iterations)