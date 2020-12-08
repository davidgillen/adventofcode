fp = open('Day8.input')
lines = fp.readlines()
pointer = 0
executed = []
acc = 0
looped = False

while not(looped):
    if pointer in executed:
        looped = True
        continue
    executed.append(pointer)
    line = lines[pointer]
    operation, argument = line.split(' ')
    if operation == 'acc':
        acc = acc + int(argument)
        pointer = pointer + 1
        continue
    elif operation == 'jmp':
        pointer = pointer + int(argument)
        continue
    elif operation == 'nop':
        pointer = pointer + 1

print(acc)
