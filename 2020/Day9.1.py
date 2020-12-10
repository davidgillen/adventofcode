fp = open('Day9.input')
lines = fp.readlines()
numlines = len(lines)

RANGE = 25

def found(num, pos):
    global RANGE, lines
    for x in range((pos - RANGE), pos-1):
        for y in range((pos - RANGE + 1), pos):
            if int(lines[x]) + int(lines[y]) == num:
                return True
    return False

for i in range(RANGE,numlines-1):
    num = int(lines[i])
    if not(found(num, i)):
        print(str(i) + ' ' + str(num))
        exit()