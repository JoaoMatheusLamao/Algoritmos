cd1 = 0
cd2 = 0
cd3 = 0
cd4 = 0
nulo = 0
branco = 0
while True:
    vt = int(input("Voto: "))
    if vt == 0:
        break
    elif vt == 1:
        cd1 += 1
    elif vt == 2:
        cd2 += 1
    elif vt == 3:
        cd3 += 1
    elif vt == 4:
        cd4 += 1
    elif vt == 5:
        nulo += 1
    elif vt == 6:
        branco += 1
    else:
        print('Erro!!!')
total = cd1 + cd2 + cd3 + cd4 + nulo + branco
print('--------------------------------')
print('Total de votos p/ candidato: ')
print(f'Candidato 1 - {cd1} votos ({(cd1/total)*100:.2f}%)')
print(f'Candidato 2 - {cd2} votos ({(cd2/total)*100:.2f}%)')
print(f'Candidato 3 - {cd3} votos ({(cd3/total)*100:.2f}%)')
print(f'Candidato 4 - {cd4} votos ({(cd4/total)*100:.2f}%)\n')
print(f"\nVotos Nulos: {nulo} ({(nulo/total)*100:.2f}%)")
print(f"\nVotos Brancos: {branco} ({(branco/total)*100:.2f}%)")
