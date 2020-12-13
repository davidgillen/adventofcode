import copy
fp = open('Day11.input')
currentSeating = []
newSeating = []
for line in fp.readlines():
    currentLine = []
    for char in line:
        if char != '\n':
            currentLine.append(char)
    currentSeating.append(currentLine)

rowCount = len(currentSeating)
colCount = len(currentSeating[0]) 


def newValue(row, col):
    global currentSeating, colcount, rowCount
    seated = 0
    empty = 0
    if currentSeating[row][col] == '.':
        return '.'

    for x in range(col-1, col+2):
        if x < 0 or x >= colCount:
            continue
        for y in range(row-1, row+2):
            if y < 0 or y >= rowCount:
                continue
            if x == col and y == row:
                continue
            if currentSeating[y][x] == '#':
                seated = seated + 1
    if currentSeating[row][col] == 'L' and seated == 0:
        return '#'
    elif currentSeating[row][col] == '#' and seated >= 4:
        return 'L'
    else:
        return currentSeating[row][col]
            
            
changed = True
while changed:
    changed = False
    newSeating.clear()
    newSeating = copy.deepcopy(currentSeating)
    for row in range(0, rowCount):
        for col in range(0, colCount):
            newSeating[row][col] = newValue(row, col)
            if newSeating[row][col] != currentSeating[row][col]:
                changed = True

    currentSeating.clear()
    currentSeating = copy.deepcopy(newSeating)

seated = 0
for row in range(0, rowCount):
    for col in range(0, colCount):
        if currentSeating[row][col] == '#':
            seated += 1
print(seated)


