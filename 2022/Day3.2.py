fp = open('input3.txt')
lines = fp.readlines()
i = 0
prioritySum = 0

while i < len(lines):
    for letter in lines[i]:
        if letter not in lines[i+1] or letter not in lines[i+2]:
            continue
        else:
            if letter >= 'a' and letter <= 'z':
                prioritySum += (ord(letter)-96)
            elif letter >= 'A' and letter <= 'Z':
                prioritySum += (ord(letter)-38)
            break
    i += 3
      
print(prioritySum)