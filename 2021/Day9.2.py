fp = open('Input9.txt')
#fp = open('Input9.sample')

basins = []
lines = fp.readlines()

def adjacentTo(x, y, basin):
    global lines
    if (x-1, y) in basin:
        return True
    if (x+1, y) in basin:
        return True
    if (x, y-1) in basin:
        return True
    if (x, y+1) in basin:
        return True
    return False


for x in range(0, len(lines)):
    for y in range(0, len(lines[0])-1):
        if lines[x][y] == '9':
            continue
        adjacent = False
        numBasins = len(basins)
        if numBasins > 0:
            for i in range(0, numBasins):
                if i >= numBasins:
                    break
                if not adjacent and adjacentTo(x, y, basins[i]):
                    basins[i].append((x,y))
                    adjacent = True
                    firstBasin = i
                    continue
                if adjacent and adjacentTo(x, y, basins[i]):
                    basins[firstBasin] += basins[i]
                    del basins[i]
                    numBasins -= 1
                
            
        if not adjacent:
            basins.append([(x,y)])
        
for basin in basins:
    print(len(basin))
