fp = open('Day10.input')
nums = [0]
for line in fp.readlines():
    nums.append(int(line))
nums.sort()
print(nums)
jump1 = 0
jump2 = 0
jump3 = 0


for i in range(1,len(nums)):
    if nums[i] - nums[i-1] == 1:
        jump1 += 1
    if nums[i] - nums[i-1] == 2:
        jump2 += 1
    if nums[i] - nums[i-1] == 3:
        jump3 += 1

print(jump1 * (jump3+1))