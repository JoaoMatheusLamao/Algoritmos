alt = float(input("Entre com a altura, em centímetros: "))
op_sexo = input('Entre com o sexo:\nM - Masculino\n'
                'F - Feminino\n')
if op_sexo.lower() == 'm':
    pideal = (72.7*alt)-58
    sexo = 'masculino'
elif op_sexo.lower() == 'f':
    pideal = (62.1*alt)-44.7
    sexo = 'feminino'
print(f'O peso ideal para uma pessoa do sexo {sexo} é: {pideal:.2f}kg')