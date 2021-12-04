fp = open('Input3.txt')
lines = fp.readlines()

counts = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in lines:
    for pos in range(0,12):
        if line[pos] == '0':
            counts[0][pos] += 1
        else:
            counts[1][pos] += 1

print(str(counts))

for pos in range(0,12):
    if counts[0][pos] > counts[1][pos]:
        gamma[pos] = '0'
        epsilon[pos] = '1'
    else:
        gamma[pos] = '1'
        epsilon[pos] = '0'

print(int(''.join(gamma),2) * int(''.join(epsilon),2))