x = float(input('Entre com o valor de x: '))
if x > 4 or x < (-4):
    fx = (5*x+3)/((x**2 - 16)**0.5)
    print('Fx = {}'.format(fx))
else:
    print('Não pode ser feita!!!')