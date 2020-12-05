fp = open('Day3.1.input.txt')
lines = fp.readlines()

ypos = 0
ychange = 1
treecount = 0
rowlength = 31
lineCount = 0

for line in lines:
    lineCount = lineCount + 1
    if lineCount % 2 == 0:
        continue
    if line[ypos] == '#':
        treecount = treecount + 1
    ypos = ypos + ychange
    if ypos >= rowlength:
        ypos = ypos - rowlength

print(treecount)