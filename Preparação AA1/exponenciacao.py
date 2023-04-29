base = float(input("Base: "))
exp = int(input("Exponente: "))

result = 1

for i in range(exp):
    result = result*base
print(result) 