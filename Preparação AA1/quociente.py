a = float(input("digite: "))
b = float(input("digite: "))

quoc = 1
while True:
    if b * quoc <= a and a - (b * quoc) < b:
        print(quoc)
        break
    else:
        quoc += 1