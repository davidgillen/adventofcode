fp = open('Day2.1.input.txt')
lines = fp.readlines()
#3-5 h: hhhshm

validcount = 0
for line in lines:
    rule, password = line.split(': ')
    minmax, letter = rule.split(' ')
    minnum, maxnum = minmax.split('-')

    count = password.count(letter)
    if ( int(minnum) <= count and count <= int(maxnum) ):
        validcount = validcount + 1

print(validcount)