# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matrizes = [[], [], [], [], []]
number = soma3Colum = somaPairs = upper2Linha = int(0)


for c in range(0, 3):

    for l in range(0, 3):
        number = int(input(f'Type the value for [{c}, {l}]: '))
        matrizes[c].append(number)

        if c == 1 and l == 0:
            upper2Linha = number
        elif c == 1 and upper2Linha < number:
            upper2Linha = number


        if l == 2:
            soma3Colum += number

        if number % 2 == 0:
            matrizes[3].append(number)
        else:
            matrizes[4].append(number)

print('-=' * 30)
for p in range(0, 3):

    for q in range(0, 3):
        print(f'[ {matrizes[p][q]:^5}', end=' ]')
    print('')



for num in matrizes[3]:
    somaPairs += num

print(f'The sum of pairs values is {somaPairs}')
print(f'The sum of the numbers in third colum is {soma3Colum}')
print(f'The upper value in the second line is {upper2Linha}')
