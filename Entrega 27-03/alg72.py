deposito = float(input('Entre com um depósito: '))
taxa = float(input('Entre com a taxa de juros: '))
rendimento = deposito*(taxa/100)
total = deposito + rendimento
print(f'Rendimentos: {rendimento}')
print(f'Total: {total}')