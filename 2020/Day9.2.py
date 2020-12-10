fp = open('Day9.input')
lines = fp.readlines()
numlines = len(lines)

TARGET = 22406676

for i in range(0,500):
    x = i
    val = 0
    smallest = int(lines[i])
    largest = int(lines[i])
    while val < TARGET:
        xval = int(lines[x])
        if xval < smallest:
            smallest = xval
        if xval > largest:
            largest = xval 
        val = val + int(lines[x])
        if val == TARGET and x > i:
            print(smallest + largest)
            exit()
        x += 1