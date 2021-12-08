#fp = open('Input8.sample')
fp = open('Input8.txt')

count = 0
for line in fp.readlines():
    wirings, outputs = line.split(' | ')
    for output in outputs.strip().split(' '):
        if len(output) in [2,3,4,7]:
            count += 1
print(count)
