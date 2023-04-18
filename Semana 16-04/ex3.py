repete = 1
n_pessoas = 0
while repete <= 10:
    idade = int(input("Entre com a idade da %dº: " %repete))
    if idade >= 18:
        n_pessoas = n_pessoas + 1
    repete += 1
print(n_pessoas)