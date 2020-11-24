# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numbers = [[],[]]

for c in range(0, 7):
    value = int(input(f'Type the {c + 1} value: '))

    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)


print(f'The pairs numbers are {sorted(numbers[0])}')
print(f'The odds numbers are {sorted(numbers[1])}')