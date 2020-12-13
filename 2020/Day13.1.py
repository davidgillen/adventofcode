import math
fp = open('Day13.input')
arrive = int(fp.readline())
schedule = fp.readline()
mintime = 9999
for bus in schedule.split(','):
    if bus == 'x':
        continue
    divides = math.floor(arrive / int(bus))
    firsttime = (divides + 1) * int(bus)
    if firsttime - arrive < mintime:
        mintime = firsttime - arrive
        answer = int(bus) * mintime
print(answer)