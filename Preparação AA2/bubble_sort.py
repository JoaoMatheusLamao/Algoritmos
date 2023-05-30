from random import randint
a = []
for i in range(20):
    a.append(randint(0, 20))

print(a)
for n in range(len(a)-1):
    for m in range(len(a)-1):
        if a[m] > a[m+1]:
            a[m], a[m+1] = a[m+1], a[m]
            
print(a)