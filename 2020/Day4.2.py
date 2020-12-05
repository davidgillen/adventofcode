import re

fp = open('Day4.1.input.txt')
lines = fp.readlines()

def validDoc(doc):
    print("#" + doc + "#")
    if ( not(re.search('byr:(19[2-9][0-9]|200(0|1|2)) ', doc))):
        return False
    if ( not(re.search('iyr:(201[0-9]|2020) ', doc))):
        return False
    if ( not(re.search('eyr:(202[0-9]|2030) ', doc))):
        return False
    if ( not(re.search('hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in) ', doc))):
        return False
    if ( not(re.search('hcl:#[0-9a-f]{6} ', doc))):
        return False
    if ( not(re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth) ', doc))):
        return False
    if ( not(re.search('pid:[0-9]{9} ', doc))):
        return False
    return True 

currentDoc = ''
validDocCount = 0
for line in lines:
    if (len(line) == 1):
        if ( validDoc(currentDoc) ):
            validDocCount = validDocCount + 1
        currentDoc = ''
        continue
    currentDoc = currentDoc + line.rstrip() + ' '

if ( validDoc(currentDoc) ):
    validDocCount = validDocCount + 1

print(validDocCount)