import math
fp = open('Day13.input')
arrive = int(fp.readline())
schedule = fp.readline()
buslist = schedule.split(',')
buses = []

class Bus:
    number = 0
    offset = 0

    def __init__(self, number, offset):
        self.number = number 
        self.offset = offset 

def checkOtherBuses(checkval):
    global buses
    for i in range(0, len(buses)-1):
        if (checkval + buses[i].offset) % buses[i].number != 0:
            return False
    return True


for i in range(0,len(buslist)):
    if buslist[i] == 'x':
        continue
    print('(x + ' + str(i) + ') mod ' + buslist[i] + ' = 0, ' )
    buses.append( Bus(int(buslist[i]), i) )
exit()
# Paste output into wolfram alpha

increment = buses[0].number
offset = 0
bus = 1
# Couldn't get to work
for bus in range(1, len(buses)):
    print('Increment: ' + str(increment))
    print('Offset: ' + str(offset))
    for x in range(offset,999999999999999, increment):
        checknum = (x * increment) + buses[bus].offset
        if checknum % buses[bus].number == 0:
            offset = checknum % (buses[bus].number * buses[bus-1].number)
            increment = increment * buses[bus].number
            print(checknum)
            break
