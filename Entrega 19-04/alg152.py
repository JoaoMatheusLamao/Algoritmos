idade = int(input('Entre com a idade do paciente: '))
peso = float(input('Entre com o peso do paciente: '))
gotas = 500/20
if peso < 5:
    print('Não pode tomar remédio porque não tem peso - Consulte um médico!')
else:
    if idade >= 12:
        if peso >= 60:
            print(f'Tomar {1000/gotas} gotas')
        else:
            print(f'Tomar {875/gotas} gotas')
    else:
        if peso <= 9:
            print(f'Tomar {125/gotas} gotas')
        elif peso <= 16:
            print(f'Tomar {250/gotas} gotas')
        elif peso <= 24:
            print(f'Tomar {375/gotas} gotas')
        elif peso <= 30:
            print(f'Tomar {500/gotas} gotas')
        else:
            print(f'Tomar {750/gotas} gotas')