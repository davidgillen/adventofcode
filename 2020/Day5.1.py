fp = open('Day5.1.input.txt')
lines = fp.readlines()

def getRowNumber(row):
    row = row.replace('F', '0')
    row = row.replace('B', '1')
    return int(row, 2)

def getSeatNumber(seat):
    seat = seat.replace('L', '0')
    seat = seat.replace('R', '1')
    return int(seat, 2)

highestSeatId = 0
seatId = 0
for line in lines:
    row = getRowNumber(line[:7])
    seat = getSeatNumber(line[7:10])
    seatId = row * 8 + seat
    if (seatId > highestSeatId):
        highestSeatId = seatId

print(highestSeatId)