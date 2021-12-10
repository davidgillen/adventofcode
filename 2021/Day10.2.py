fp = open('Input10.txt')
#fp = open('Input10.sample')

openers = ['(','[','{','<']
incompleteLines = []
for line in fp.readlines():
    chars = [line[0]]
    errorFound = False
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
            errorFound = True
            break
    if not errorFound:
        incompleteLines.append(line.strip())

scores = []
for line in incompleteLines:
    removed = True
    while removed:
        if '()' in line:
            line = line.replace('()','')
        elif '[]' in line:
            line = line.replace('[]','')
        elif '{}' in line:
            line = line.replace('{}','')
        elif '<>' in line:
            line = line.replace('<>','')
        else:
            removed = False
    
    lineScore = 0
    while(len(line) > 0):
        if line[-1] == '(':
            lineScore = lineScore * 5 + 1
        if line[-1] == '[':
            lineScore = lineScore * 5 + 2
        if line[-1] == '{':
            lineScore = lineScore * 5 + 3
        if line[-1] == '<':
            lineScore = lineScore * 5 + 4
        line = line[0:-1]
    scores.append(lineScore)

scores.sort()
print(scores[int(round(len(scores)/2))])

