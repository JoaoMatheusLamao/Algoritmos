n = int(input('Digite: '))


# cont_h = 1
# binario_h = 0
# while cont_h <= n:
#     if binario_h == 0:
#         h = h + ((n*2)-1)/n
#         binario_h = 1
#         cont_h += 1
#     else:
#         h = h - ((n*2)-1)/n
#         binario_h = 0
#         cont_h += 1
        
h = 0
binario = 0
for i in range(1, n + 1):
    if binario == 0 and h == 0:
        h = h + (i*2-1)/i
    elif binario == 0:
        binario = 1
        h = h + (i*2-1)/i
    else:
        binario = 0
        h = h - (i*2-1)/i


s = 0
binario = 0
for i in range(1, n + 1):
    if binario == 0 and s == 0:
       s = s + i/(i*i)
    elif binario == 0:
        binario = 1
        s = s + i/(i*i)
    else:
        binario = 0
        s = s - i/(i*i)



# s = 1
# cont_s = 1
# binario_s = 0
# while cont_s <= n:
#     if binario_s == 0:
#         s = s + n/(n**2)
#         binario_s = 1
#         cont_s += 1
#     else:
#         s = s - n/(n**2)
#         binario_s = 0
#         cont_s += 1
        
        
print(f'H = {h}')
print(f'S = {s}')



# p = 0
# cont_p = 2
# cont_p_base = 1
# for i in range(1, n):
#     p = p + cont_p/(cont_p_base**3)
#     cont_p = cont_p_base
#     cont_p += 2


