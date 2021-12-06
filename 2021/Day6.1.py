#fp = open('Input6.sample')
fp = open('Input6.txt')

lanterns = [0]*9
print(lanterns)
for num in fp.readline().split(','):
    print(num)
    lanterns[int(num)] += 1

for i in range(0,256):
    spawning = lanterns[0]
    for j in range(1,9):
        lanterns[j-1] = lanterns[j]
    lanterns[8] = spawning
    lanterns[6] += spawning

count = 0
for x in lanterns:
    count += x

print(lanterns)
print(count)
