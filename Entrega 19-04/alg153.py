indice = float(input('Entre com om índice de poluição: '))
if indice >= 0.5:
    print("Supender as atividades das indústrias dos grupos 1, 2 e 3!!!")
elif indice >= 0.4:
    print("Supender as atividades das indústrias dos grupos 1 e 2!!!")
elif indice >= 0.3:
    print("Supender as atividades das indústrias do grupo 1!!!")
else:
    print("Índice de poluição aceitável para todos os grupos!")