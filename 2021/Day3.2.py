#fp = open('Input3.sample')
fp = open('Input3.txt')
lines = fp.readlines()
lineSize = len(lines[0].strip())

gamma = [0]*lineSize
epsilon = [0]*lineSize

def getCounts(lineSize, lines):
    counts = [[0]*lineSize,[0]*lineSize]
    for line in lines:
        for pos in range(0,lineSize):
            if line[pos] == '0':
                counts[0][pos] += 1
            else:
                counts[1][pos] += 1
    return counts

counts = getCounts(lineSize, lines)

oxCounts = counts
scrubCounts = counts
oxLines = lines
scrubLines = lines
newOxgen = []
newScrubber = []
for pos in range(0,lineSize):
    if oxCounts[0][pos] > oxCounts[1][pos]:
        for line in oxLines:
            if line[pos] == '0':
                newOxgen.append(line)
            
    else: # Handles cases where more 1s or equal 1s and 0s.
        for line in oxLines:
            if line[pos] == '1':
                newOxgen.append(line)
    if len(newOxgen) == 1:
        break
    oxLines = newOxgen
    newOxgen = []
    oxCounts = getCounts(lineSize, oxLines)

oxgenRating = int(newOxgen[0].strip(), 2)

for pos in range(0,lineSize):
    if scrubCounts[0][pos] > scrubCounts[1][pos]:
        for line in scrubLines:
            if line[pos] == '1':
                newScrubber.append(line)
            
    else: # Handles cases where more 1s or equal 1s and 0s.
        for line in scrubLines:
            if line[pos] == '0':
                newScrubber.append(line)
    if len(newScrubber) == 1:
        break
    scrubLines = newScrubber
    newScrubber = []
    scrubCounts = getCounts(lineSize, scrubLines)

scrubberRating = int(newScrubber[0].strip(), 2)

print(oxgenRating * scrubberRating)