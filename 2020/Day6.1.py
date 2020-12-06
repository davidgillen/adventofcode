fp = open('Day6.1.input')
lines = fp.readlines()

sum = 0
yes = {}
for line in lines:
    if len(line.rstrip()) == 0:
        sum = sum + len(yes)
        yes.clear()
        continue
    for char in line.rstrip():
        if(char != '\n'):
            yes[char] = True

sum = sum + len(yes)
print(sum)
