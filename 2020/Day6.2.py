fp = open('Day6.1.input')
lines = fp.readlines()

sum = 0
base = []
newSet = True
for line in lines:
    if len(line.rstrip()) == 0:
        sum = sum + len(base)
        base.clear()
        newSet = True
        continue
    if newSet == True:
        for char in line.rstrip():
            base.append(char)
        newSet = False
    
    subsequent = []
    for char in line.rstrip():
        subsequent.append(char)
    base = list(set(base).intersection(subsequent))

sum = sum + len(base)
print(sum)