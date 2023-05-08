def digitVerificador(conta):
    inv_conta = int(str(conta)[::-1])
    soma = str(conta+inv_conta)
    
    x = 1
    y=0
    for num in soma:
       y += int(num)*x 
       x+=1
    return str(y)[-1]
    

digito = digitVerificador(25678)
print(digito)