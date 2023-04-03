vaplica = float(input("Digite o valor da aplicação: "))
vtaxa = float(input('Digite a taxa (0-1): '))
meses = int(input('Entre com o número de meses: '))
vacumulado = vaplica*(((1 + vtaxa)**meses)-1)/vtaxa
print(f'O valor acumulado é de: R$ {vacumulado:.2f}')