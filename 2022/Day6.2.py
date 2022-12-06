fp = open('input6.txt')
line = fp.readline()
i = 0
marker = 14
while i < (len(line)-marker):
    snippet = line[i:i+marker]
    j = 0
    while j < marker:
        if snippet.count(snippet[j]) > 1:
            break
        j += 1
    if j == marker:
        print('HERE: ' + str(i+marker))
        exit()
    i += 1