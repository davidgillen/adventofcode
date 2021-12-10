fp = open('Input10.txt')
#fp = open('Input10.sample')

openers = ['(','[','{','<']

syntaxErrorScore = 0
for line in fp.readlines():
    chars = [line[0]]
    for i in range(1, len(line.strip())):
        if line[i] in openers:
            chars.append(line[i])
        elif chars[-1] == '(' and line[i] == ')':
            chars.pop()
        elif chars[-1] == '[' and line[i] == ']':
            chars.pop()
        elif chars[-1] == '{' and line[i] == '}':
            chars.pop()
        elif chars[-1] == '<' and line[i] == '>':
            chars.pop()
        else:
            if line[i] == ')':
                syntaxErrorScore += 3
            if line[i] == ']':
                syntaxErrorScore += 57
            if line[i] == '}':
                syntaxErrorScore += 1197
            if line[i] == '>':
                syntaxErrorScore += 25137
            break

print(syntaxErrorScore)