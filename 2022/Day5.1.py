crates = [[],
    ['G','T','R','W'],
    ['G','C','H','P','M','S','V','W'],
    ['C','L','T','S','G','M'],
    ['J','H','D','M','W','R','F'],
    ['P','Q','L','H','S','W','F','J'],
    ['P','J','D','N','F','M','S'],
    ['Z','B','D','F','G','C','S','J'],
    ['R','T','B'],
    ['H','N','W','L','C']
]

fp = open('input5.txt')
lines = fp.readlines()

for line in lines:
    parts = line.strip().split(' ')

    i = int(parts[1])
    while i > 0:
        crate = crates[int(parts[3])].pop()
        crates[int(parts[5])].append(crate)
        i -= 1

print(crates)