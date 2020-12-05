fp = open('Day2.1.input.txt')
lines = fp.readlines()

validcount = 0
for line in lines:
    rule, password = line.split(': ')
    minmax, letter = rule.split(' ')
    minnum, maxnum = minmax.split('-')

    count = password.count(letter)
    if len(password) >= int(maxnum):
        firstPosition = password[int(minnum)-1]
        secondPosition = password[int(maxnum)-1]
        if ( firstPosition == letter and secondPosition != letter ):
            validcount = validcount + 1
        if ( firstPosition != letter and secondPosition == letter ):
            validcount = validcount + 1
    else:
        if ( firstPosition == letter ):
            validcount = validcount + 1

print(validcount)