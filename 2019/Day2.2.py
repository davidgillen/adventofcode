fp = open('Day2.input')
lines = fp.readlines()
opCodes = lines[0].split(',')
codes = []

for code in opCodes:
    codes.append(int(code))

def calcOutput(x, y, codes):
    position = 0
    finished = False
    codes[1] = x
    codes[2] = y
    while not(finished):
        code = codes[position]
        firstParam = codes[position+1]
        secondParam = codes[position+2]
        target = codes[position+3]
        if code == 99:
            finished = True
            continue
        if code == 1:
            codes[target] = codes[firstParam] + codes[secondParam]
        if code == 2:
            codes[target] = codes[firstParam] * codes[secondParam]
        position = position + 4
    return codes[0]

for x in range(100):
    for y in range(100):
        result = calcOutput(x, y, codes.copy())
        if result == 19690720:
            print(x* 100 + y)
            exit()