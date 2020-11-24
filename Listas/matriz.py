# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrizes = [[],[],[]]
number = int()
for c in range(0, 3):

    for l in range(0, 3):
        number = int(input(f'Type the value for [{c}, {l}]: '))
        matrizes[c].append(number)

print('-=' * 30)
for p in range(0, 3):

    for q in range(0, 3):
        print(f'[ {matrizes[p][q]:^5}', end=' ]')
    print()
