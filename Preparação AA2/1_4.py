from random import randint 

nums = []
for i in range(20):
    nums.append(randint(0, 10))
print(f'\n{nums}\n')
nums_ordenado = []

for i in range(20):
    nums_ordenado.append(min(nums))
    nums.remove(min(nums))

print(nums_ordenado)
