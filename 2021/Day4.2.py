#fp = open('Input4.sample')
fp = open('Input4.txt')
numbers = fp.readline().strip().split(',')
fp.readline() # /just discard this
cards = []
nextCard = []

line = fp.readline()
while len(line) > 0:
    if line == '\n':
        cards.append(nextCard)
        nextCard = []
    else:
        nextCard.append(line.strip().replace('  ', ' ').split(' '))
    line = fp.readline()

cards.append(nextCard)

def markCard(card, num):
    for row in range(0,len(card)):
        for space in range(0, len(card[row])):
            if card[row][space] == num:
                card[row][space] = '#'
    return card

def checkWinner(card):
    for row in card:
        if checkRow(row):
            return True
    for i in range(0,5):
        if checkRow([card[0][i], card[1][i], card[2][i], card[3][i], card[4][i]]):
            return True
    return False

def checkRow(row):
    for space in row:
        if space != '#':
            return False
    return True

def calculateScore(card, num):
    sum = 0
    for row in card:
        for space in row:
            if space != '#':
                sum += int(space)
    result = int(num) * sum
    return result

winners = []
lastToWin = False
for num in numbers:
    for i in range(0, len(cards)):
        if i in winners:
            continue
        cards[i] = markCard(cards[i], num)
        if checkWinner(cards[i]):
            winners.append(i)
            if len(winners) == len(cards):
                print(num)
                print(calculateScore(cards[i], num))
                exit()
