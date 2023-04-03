print('Cálculo de juros simples!!!')
print('-------------------------------------')
cpi = float(input('Entre com o capital inicial, em reais: '))
tx = float(input('Entre com o taxa de juros, em porcentagem: '))
periodo = float(input('Entre com o periodo, em meses: '))
print('-------------------------------------')
j = cpi * (tx/100) * periodo
print(f'O total de juros simples é R${j}')
print('-------------------------------------')