nome = input('Entre com o nome do paciente: ')
peso = float(input('Entre com o peso, em kg: '))
alt = float(input('Entre com a altura, em metros: '))
imc = peso/alt**2
if imc < 20:
    fx_risco = 'Abaixo do peso'
elif imc <= 25:
    fx_risco = 'Normal'
elif imc <= 30:
    fx_risco = 'Excesso de peso'
elif imc <= 35:
    fx_risco = 'Obesidade'
else:
    fx_risco = 'Obesidade mórbida'  
print(f'Paciente: {nome}\n'
      f'Faixa de risco: {fx_risco}')