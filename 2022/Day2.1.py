fp = open('input2.txt')
lines = fp.readlines()
total = 0

for line in lines:
    opponent, me = line.split(' ')
    if me[0] == 'X':
        total += 1
        if opponent == 'A':
            total += 3
        elif opponent == 'B':
            total += 0
        elif opponent == 'C':
            total += 6
    elif me[0] == 'Y':
        total += 2
        if opponent == 'A':
            total += 6
        elif opponent == 'B':
            total += 3
        elif opponent == 'C':
            total += 0
    elif me[0] == 'Z':
        total +=3
        if opponent == 'A':
            total += 0
        elif opponent == 'B':
            total += 6
        elif opponent == 'C':
            total += 3

print(total)

