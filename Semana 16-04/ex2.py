n = int(input('Entre com um número: '))
s = 0
if n > 0:
    for i in range(1, n+1):
        s = s + 1/i
print(s)