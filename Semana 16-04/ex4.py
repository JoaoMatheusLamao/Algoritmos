pessoa = 1

pes_maior50anos_menor60kg = 0
cont_menor_150 = 0
cont_olhos_azuis = 0
pessoas_ruivas_sem_azul = 0
ac_idade = 0
while pessoa <= 5:
    idade = int(input(f"Entre com a idade da {pessoa}ª pessoa: "))
    peso = float(input(f"Entre com o peso da {pessoa}ª pessoa: "))
    alt = float(input(f"Entre com a altura da {pessoa}ª pessoa, em centímetros: "))
    cor_olhos = (input('Entre com a cor dos olhos: ')).lower()
    cor_cabelo = (input('Entre com a cor dos cabelos: ')).lower()
    
    if idade > 50 and peso < 60:
        pes_maior50anos_menor60kg += 1
    if alt < 150:
        cont_menor_150 += 1
        ac_idade += idade
    if cor_olhos == 'a':
        cont_olhos_azuis += 1
    if cor_olhos != 'a' and cor_cabelo == 'r':
        pessoas_ruivas_sem_azul += 1
    pessoa+=1
if cont_menor_150 > 0:
    media_idade_menor_150 = ac_idade/cont_menor_150
    
percentual_olhos_azuis = (cont_olhos_azuis/20)*100


print(f"Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos: {pes_maior50anos_menor60kg}")
print(f"Média das idades das pessoas com altura inferior a 1,50: {media_menor_150:.2f}")
print(f"A percentagem de pessoas com olhos azuis entre todas as analisadas é: {percentual_olhos_azuis}")
print(f"A quantidade de pessoas ruivas e que não possuem olhos azuis é: {pessoas_ruivas_sem_azul}")