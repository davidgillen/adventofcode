fp = open('Day2.input')
lines = fp.readlines()
opCodes = lines[0].split(',')
codes = []

for code in opCodes:
    codes.append(int(code))
position = 0
finished = False

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

print(codes[0])