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

    crates[int(parts[5])].extend( crates[int(parts[3])][-int(parts[1]):] )
    crates[int(parts[3])] = crates[int(parts[3])][0:-int(parts[1])]

print(crates)