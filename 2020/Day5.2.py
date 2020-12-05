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

seatIds = []
for line in lines:
    row = getRowNumber(line[:7])
    seat = getSeatNumber(line[7:10])
    seatId = row * 8 + seat
    seatIds.append(seatId)

seatIds.sort()

for seatId in seatIds:
    if ( not((seatId+1) in seatIds) and (seatId+2) in seatIds):
        print(seatId+1)