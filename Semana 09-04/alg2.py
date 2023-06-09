tpComb = int(input('Entre com o tipo de combustível:\n'
                   '1-Gasolina\n'
                   '2-Álcool\n'))
litros = float(input("Entre com a quantidade de litros abastecido: "))
#identificando o combustível
if tpComb == 1:
    vlComb = 3.3
elif tpComb == 2:
    vlComb = 2.9

#identificando o valor de desconto para alcool
if litros <= 20:
    descont = 0.97 
elif litros > 20:
    descont = 0.95
#identificando o valor de desconto para alcool
if litros <= 20:
    descont = 0.96
elif litros > 20:
    descont = 0.94
    
#cálculo
total = (vlComb*descont)*litros

#exibindo o resultado
print(f'O valor total é: R${total:.2f}')