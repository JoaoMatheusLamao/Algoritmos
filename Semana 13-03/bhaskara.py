print('')
print('Calculando Bhaskara')
print('Fórmula: Ax² + Bx + C = 0')
print('----------------------------')
a = float(input('Entre com o valor de *A*: '))
b = float(input('Entre com o valor de *B*: '))
c = float(input('Entre com o valor de *C*: '))
print('')
delta = b**2 - 4 *a *c
if delta < 0:
    print('O discriminante é negativo, portanto sua equação não possui raízes reais!')
elif a == 0:
    print('O *A* é igual a zero, portanto sua equação não possui raízes reais!')
else:
    x1 = (-b + (delta**0.5))/(2*a)
    x2 = (-b - (delta**0.5))/(2*a)
    print(f'X1 é igual a: {x1}')
    print(f'X2 é igual a: {x2}')
print('----------------------------') 