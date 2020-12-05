# Load the file
fp = open('Day1.1.input.txt')
lines = fp.readlines()

count = 0
for x in range(0, len(lines)-1):
    for y in range(x+1, len(lines)):
        count = count + 1
        if (int(lines[x]) + int(lines[y])) == 2020:
            print(lines[x])
            print(lines[y])
            print(int(lines[x]) * int(lines[y]))

print(count)

# Check values against each other

