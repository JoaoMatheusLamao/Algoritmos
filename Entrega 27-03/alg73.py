num = float(input('Entre com um número decimal: '))
numint = int(num)
numfrac = num - numint
numaprox = int(num + 0.5)
print(f"Número inteiro: {numint}")
print(f"Número fracionário: {numfrac:.2f}")
print(f"Número arredondado: {numaprox}")