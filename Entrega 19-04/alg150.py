from math import sin, cos, pi

ang = float(input('Entre com o ângulo, em graus: '))
rang = ang * 3.14 / 180
if ((rang > pi/2 and rang <= pi) or (rang > 3*pi/2 and rang <= 2 * pi)):
    print(f'Seno: {sin(rang):.2f}')
else:
    print(f'Coseno: {cos(rang):.2f}')