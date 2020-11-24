# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

values = list()

for cont in range (0,5):
    number = int(input('Type a value: '))
    if cont == 0 or number > values[-1]:
        values.append(number)
    else:
        pos = 0
        while pos < len(values):
            if number <= values[pos]:
                values.insert(pos, number)
                break
            pos += 1



print(values)
