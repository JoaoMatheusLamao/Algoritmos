from random import randint

nums = []
for i in range(20):
    nums.append(randint(0, 10))
print(f'\n{nums}\n')

for a in range(len(nums)-1):
    for b in range(len(nums)-1):
        if nums[b] > nums[b+1]:
            nums[b], nums[b+1] = nums[b+1], nums[b]

print(f'\n{nums}\n')