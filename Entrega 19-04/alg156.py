dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
if ano >= 1:
    vd = 1
    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        vd = 0
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        vd = 0
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                vd = 0
        else:
            if dia > 28:
                vd = 0
else:
    vd = 0
if vd == 0:
    print('Data inválida')
else:
    print('Data válida')