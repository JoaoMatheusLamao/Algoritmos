from random import randint, random

# 1. Leia um vetor de 10 elementos e calcule o maior e o menor valor.

def one():
    nr_el = 10
    el = []
    for i in range(0, nr_el):
        el.append(randint(0, 100))
    print(el)
    print(f'O maior elemento: {max(el)}')
    print(f'O menor elemento: {min(el)}')

# one()


# 2. Agora usando listas, indique como um troco deve ser dado utilizando-se um número mínimo de
# notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado
# desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1
# reais, e que nenhuma delas esteja em falta no caixa.

def two():
    vl_ct = int(input('Valor da conta: '))
    vl_pg = int(input('Valor da pago: '))
    troco = vl_pg - vl_ct
    notas = [50, 20, 10, 5, 2, 1]
    resultado = []

    for nota in notas:
        quantidade = troco // nota
        if quantidade > 0:
            resultado.append((nota, quantidade))
            troco -= nota * quantidade

    for i in resultado:
        print(f'{i[1]} notas de R$ {i[0]},00;')
# two()

# 3. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
# números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def three():
    nums = []
    par = []
    impares = []
    for i in range(20):
        numero = randint(1, 100)
        nums.append(numero)
        if numero%2 == 0:
            par.append(numero)
        else:
            impares.append(numero)

    print(f"Números: {nums}")
    print(f"Pares: {par}")
    print(f"Ímpares: {impares}")
# three()


# 4. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def four():
    medias = []
    for i in range(10):
        notas = []
        for j in range(4):
            notas.append(randint(0, 10))
        medias.append(sum(notas)/len(notas))
    # print(medias)
    medias_maior_sete = 0
    for i in medias:
        if i >= 7:
            medias_maior_sete += 1
    print(f"Número de alunos com média maior ou igual a 7.0:\t{medias_maior_sete} alunos")
# four()


# 5. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
# os números.

def five():
    nums = []
    multiplicacao = 1
    for i in range(5):
        num = randint(0, 10)
        nums.append(num)
        multiplicacao *= num


    print(f"Soma:\t{sum(nums)}")
    print(f"Multiplicação:\t{multiplicacao}")
    print(f"Números:\t{nums}")
# five()


# 6. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
# seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.


# 7. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.

def seven():
    nums = []
    soma = 0
    for i in range(10):
        numero = randint(1, 100)
        nums.append(numero)
        soma += numero**2

    print(f"Números: {nums}")
    print(f"Soma: {soma}")
# seven()



# 8. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros
# vetores.

def eight():
    a = []
    b = []
    c = []
    for i in range(10):
        a.append(randint(0, 100))
        b.append(randint(0, 100))
        c.extend([a[i], b[i]])
    print(a)
    print(b)
    print(c)
# eight()


# 9. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


# 10.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em
# uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas
# acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro,
# 2 – Fevereiro, . . . ).