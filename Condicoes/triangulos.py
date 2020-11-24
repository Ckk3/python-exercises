# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

side1 = float(input('Type the first segment: '))
side2 = float(input('Type the second segment: '))
side3 = float(input('Type the third segment: '))

if side3 < (side1 + side2) and side2 < (side1 + side3) and side1 < (side2 + side3):
    print('A triangle can be construct!!')
else:
    print('A triangle cant be construct.')
    