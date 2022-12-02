fp = open('input2.txt')
lines = fp.readlines()
total = 0

for line in lines:
    opponent, me = line.split(' ')
    if me[0] == 'X':
        total += 0
        if opponent == 'A':
            total += 3
        elif opponent == 'B':
            total += 1
        elif opponent == 'C':
            total += 2
    elif me[0] == 'Y':
        total += 3
        if opponent == 'A':
            total += 1
        elif opponent == 'B':
            total += 2
        elif opponent == 'C':
            total += 3
    elif me[0] == 'Z':
        total +=6
        if opponent == 'A':
            total += 2
        elif opponent == 'B':
            total += 3
        elif opponent == 'C':
            total += 1

print(total)

