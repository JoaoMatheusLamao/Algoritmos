a = float(input("Primeiro termo: "))
b = float(input("Segundo termo: "))

print(a)
print(b)

for i in range(18):
    prox = a+b
    print(prox)
    a = b
    b = prox