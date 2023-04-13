pal = input('Entre com uma palavra: ')
letra1 = pal[0].lower()
if letra1 == 'l' or letra1 == 'd':
    nv_pal = pal[0:1], pal[-1]
else:
    nv_pal = pal[1:]
print(f'Nova palavra: {nv_pal}')