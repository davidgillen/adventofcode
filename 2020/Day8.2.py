fp = open('Day8.input')
lines = fp.readlines()
maxpointer = len(lines)
pointer = 0
executed = []
acc = 0
looped = False
finished = False
changed = []
oneChanged = False

def reset():
    global pointer
    pointer = 0
    global executed
    executed.clear()
    global acc
    acc = 0
    global looped
    looped = False
    global oneChanged
    oneChanged = False

while not(looped) and not(finished):
    if pointer in executed:
        reset()
        continue
    if pointer >= maxpointer:
        finished = True
        continue
    executed.append(pointer)
    line = lines[pointer]
    operation, argument = line.split(' ')
    if not(oneChanged) and operation == 'nop' and not(pointer in changed):
        operation = 'jmp'
        changed.append(pointer)
        oneChanged = True
    elif not(oneChanged) and operation == 'jmp' and not(pointer in changed):
        operation = 'nop'
        changed.append(pointer)
        oneChanged = True

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