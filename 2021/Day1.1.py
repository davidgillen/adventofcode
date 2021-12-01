fp = open('Input1.1.txt')
lines = fp.readlines()

previous = 99999999
count = 0
for line in lines:
    if int(line) > int(previous):
        count+=1
    previous = line

print(count)