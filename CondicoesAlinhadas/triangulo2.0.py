'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''


side1 = float(input('Type the first segment: '))
side2 = float(input('Type the second segment: '))
side3 = float(input('Type the third segment: '))

if side3 < (side1 + side2) and side2 < (side1 + side3) and side1 < (side2 + side3):
    print('\nA triangle can be construct!!')
    if side1 == side2 == side3:
        print('Its  is a Equilateral triangle!')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('Its a Isoceles triangle!')
    else:
        print('Its a scalene triangle!')
else:
    print('\nA triangle cant be construct.')