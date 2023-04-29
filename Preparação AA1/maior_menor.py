conj = []
while True:    
    num = int(input("Digite: "))
    if num >= 0:
        conj.append(num)
    else:
        print(f"Maior valor: {max(conj)}")
        print(f"Menor valor: {min(conj)}")