fp = open('Day7.input.txt')
lines = fp.readlines()

#light red bags contain 1 bright white bag, 2 muted yellow bags.
#faded blue bags contain no other bags.

rules = {}
for line in lines:
    outer, contains = line.split('s contain ')
    inner = contains[:-1].split(', ')
    rules[outer] = {}
    for bag in inner:
        count, bagType = bag.split(' ', 1)
        bagType = bagType.replace('bags', 'bag').replace('.', '')
        rules[outer][bagType] = count



def countBags(rule):
    count = 1
    for subrule in rules[rule]:
        if subrule == 'other bag':
            return 1
        count = count + int(rules[rule][subrule]) * countBags(subrule)
    return count


print(countBags('shiny gold bag')-1)