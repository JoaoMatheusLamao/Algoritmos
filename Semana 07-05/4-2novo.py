def reverseNum(num):
    return str(num)[::-1]
# print(reverseNum(1479))

def digVerif(num):
    num_revers = int(str(num)[::-1])
    soma = str(num + num_revers)
    
    acumulador = 0
    x=1
    for num in soma:
        acumulador += int(num)*x
        x+=1

    return str(acumulador)[-1]
print(digVerif(25678))