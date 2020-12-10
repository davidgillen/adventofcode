fp = open('Day10.input')
nums = [0]
for line in fp.readlines():
    nums.append(int(line))
nums.sort()
print(nums)
jump1 = 0
jump2 = 0
jump3 = 0
jump4 = 0

pos = 0
while pos < len(nums):
    count = 0
    nextpos = pos+1
    if nextpos >= len(nums):
        break
    while nums[nextpos] - nums[nextpos-1] == 1:
        count +=1
        nextpos += 1
        if nextpos >= len(nums):
            break
    if count == 2:
        jump2 += 1    
    if count == 3:
        jump3 += 1    
    if count == 4:
        jump4 += 1
    pos = nextpos

print(jump2)
print(jump3)
print(jump4)
print(pow(2,jump2) *  pow(4,jump3) * pow(7, jump4))