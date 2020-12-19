import re

def calculate(sumstr):
    p = re.compile('.*(\([0-9\+\* ]+\)).*')
    while '(' in sumstr:
        m = p.match(sumstr)
        replace = m.group(1)
        subsum = m.group(1).replace('(','').replace(')','')
        subans = calculate(subsum)
        sumstr = sumstr.replace(replace, str(subans))
    parts = sumstr.split(' ')
    
    i=1
    while len(parts) > 1 and i < len(parts):
        if parts[i] == '+':
            plus = int(parts[i-1]) + int(parts[i+1])
            del parts[i]
            del parts[i]
            parts[i-1] = plus
            continue
        else:
            i += 2

    i = 1
    while len(parts) > 1 and i < len(parts):
        if parts[i] == '*':
            plus = int(parts[i-1]) * int(parts[i+1])
            del parts[i]
            del parts[i]
            parts[i-1] = plus
            continue
        else:
            i += 2
    return parts[0]

fp = open('Day18.input')
sum = 0
for line in fp.readlines():
    sum += calculate(line)
print(sum)
#print(calculate('1 + (2 * 3) + (4 * (5 + 6))'))
#print(calculate('2 * 3 + (4 * 5)'))
#print(calculate('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
#print(calculate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
#print(calculate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))

