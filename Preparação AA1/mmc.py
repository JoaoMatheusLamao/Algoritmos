a = int(input("Digite: "))
b = int(input("Digite: "))

if a > b:
    maior = a
else:
    maior = b
    
while True:
    if maior % a == 0 and maior % b == 0:
        print(maior)
        break
    else:
        maior+=1