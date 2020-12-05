# Load the file
fp = open('Day1.1.input.txt')
lines = fp.readlines()

count = 0
for x in range(0, len(lines)-2):
    for y in range(x+1, len(lines)-1):
        count = count + 1
        if (int(lines[x]) + int(lines[y])) < 1754:
            for z in range(x+2, len(lines)):
                if (int(lines[x]) + int(lines[y]) + int(lines[z])) == 2020:
                    print(lines[x])
                    print(lines[y])
                    print(lines[z])
                    print(int(lines[x]) * int(lines[y]) * int(lines[z]))

print(count)