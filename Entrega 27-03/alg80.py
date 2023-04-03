qtdfitas = int(input('Digite a quantidade de fitas: '))
valuguel = float(input('Digite o valor do aluguel: '))
fatanual = qtdfitas/3 * valuguel * 12
print(f'Faturamento anual: {fatanual}')
multas = valuguel * 0.1 * (qtdfitas/3)/10
print(f'Multas mensais: {multas}')
qtdfinal = qtdfitas - qtdfitas*0.02 + qtdfitas/10
print(f'Quantidades de fitas ao final do ano: : {qtdfinal}')