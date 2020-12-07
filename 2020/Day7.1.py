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


containsGold = {}

def checkContainsGold(rule):
    for subrule in rules[rule]:
        if subrule == 'other bag':
            containsGold[subrule] = False
            continue
        elif subrule == 'shiny gold bag':
            containsGold[rule] = True
            return True
        elif subrule in containsGold:
            if containsGold[subrule]:
                containsGold[rule] = True
                return True
        else:
            if checkContainsGold(subrule):
                containsGold[subrule] = True
                containsGold[rule] = True
                return True
    return False



for rule in rules:
    if rule in containsGold:
        continue
    else:
        checkContainsGold(rule)

print(containsGold)

count = 0
for check in containsGold:
    if containsGold[check]:
        count = count + 1
print(count)