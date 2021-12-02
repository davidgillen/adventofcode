fp = open('Input2.txt')
lines = fp.readlines()

depth = 0
distance = 0
for line in lines:
    dir, dist = line.split(' ')
    if dir == 'forward':
        distance += int(dist)
    if dir == 'down':
        depth += int(dist)
    if dir == 'up':
        depth -= int(dist)

print(depth * distance)