fp = open('Input1.1.txt')
lines = fp.readlines()

count = 0
for x in range(0, len(lines)-3):
    a = int(lines[x]) + int(lines[x+1]) + int(lines[x+2])
    b = int(lines[x+1]) + int(lines[x+2]) + int(lines[x+3])

    if b > a:
        count+=1

print(count)