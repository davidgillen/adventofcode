fp = open('Input2.txt')
lines = fp.readlines()

depth = 0
aim = 0
distance = 0
for line in lines:
    dir, dist = line.split(' ')
    if dir == 'forward':
        distance += int(dist)
        depth += (aim * int(dist))
    if dir == 'down':
        aim += int(dist)
    if dir == 'up':
        aim -= int(dist)

print(depth * distance)