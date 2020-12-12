fp = open('Day12.input')
xpos = 0
ypos = 0
dir = 'E'

def changeDir(turn):
    global dir
    dirs = ['N','E','S','W']
    if turn[0] == 'L':
        direction = -1
    elif turn[0] == 'R':
        direction = 1
    amount = int(turn[1:])
    while amount > 0:
        amount -= 90
        index = dirs.index(dir) + direction
        if index < 0:
            index = 3
        elif index > 3:
            index = 0
        dir = dirs[index]

def move(movement):
    global xpos, ypos
    xchange = 0
    ychange = 0
    if movement[0] == 'N':
        ychange = 1
    elif movement[0] == 'S':
        ychange = -1
    elif movement[0] == 'E':
        xchange = 1
    elif movement[0] == 'W':
        xchange = -1
    else:
        exit('Invalid direction')
    distance = int(movement[1:])
    xpos += (xchange*distance)
    ypos += (ychange*distance)

def forward(movement):
    global dir
    move(movement.replace('F', str(dir)))

for line in fp.readlines():
    if line[0] == 'L' or line[0] == 'R':
        changeDir(line)
    elif line[0] == 'F':
        forward(line)
    else:
        move(line)

print(abs(xpos) + abs(ypos))
