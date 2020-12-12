fp = open('Day12.input')
xpos = 0
ypos = 0
xway = 10
yway = 1

def rotateWayPoint(turn):
    global xway, yway
    if turn[0] == 'R':
        rotateWayPoint('L' + str(360 - int(turn[1:])))
        return
    amount = int(turn[1:])
    while amount > 0:
        amount -= 90
        newx = -1 *yway
        newy = xway
        xway = newx
        yway = newy

def moveWayPoint(movement):
    global xway, yway
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
    xway += (xchange*distance)
    yway += (ychange*distance)

def forward(movement):
    global xpos, ypos, xway, yway
    distance = int(movement[1:])
    xpos += (xway * distance)
    ypos += (yway * distance)

for line in fp.readlines():
    if line[0] == 'L' or line[0] == 'R':
        rotateWayPoint(line)
    elif line[0] == 'F':
        forward(line)
    else:
        moveWayPoint(line)

print(abs(xpos) + abs(ypos))