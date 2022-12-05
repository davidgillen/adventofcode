fp = open('input4.txt')
lines = fp.readlines()

needAttention = 0
for line in lines:
    e1, e2 = line.split(',')
    e1s, e1f = e1.split('-')
    e2s, e2f = e2.split('-')

    if int(e1s) <= int(e2s) and int(e1f) >= int(e2f):
        needAttention += 1
    elif int(e2s) <= int(e1s) and int(e2f) >= int(e1f):
        needAttention += 1
    
print(needAttention)
