fp = open('input3.txt')
lines = fp.readlines()

prioritySum = 0
for line in lines:
    line = line.strip()
    left = line[0: int(len(line)/2)]
    right = line[int(len(line)/2):]
    for letter in left:
        if letter not in right:
            continue
        else:
            if letter >= 'a' and letter <= 'z':
                prioritySum += (ord(letter)-96)
            elif letter >= 'A' and letter <= 'Z':
                prioritySum += (ord(letter)-38)
            break
       
print(prioritySum)