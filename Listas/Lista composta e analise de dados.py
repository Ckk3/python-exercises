#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

people = list()
current = list()
light = float()
heavy = float()
lightList = list()
heavyList = list()
totPeople = int(0)
answer = str('s')

while answer == 's':

    current.append(str(input('Type a name: ')).strip())
    current.append(float(input('Type the mass: ')))

    if totPeople == 0:
        light = heavy = current[1]
        lightList.append(current[:])
        heavyList.append(current[:])
    else:
        if current[1] > heavy:
            heavy = current[1]
            heavyList.clear()
            heavyList.append(current[:])

        elif current[1] == heavy:
            heavyList.append(current[:])

        elif current[1] < light:
            light = current[1]
            lightList.clear()
            lightList.append(current[:])

        elif current[1] == light:
            lightList.append(current[:])

    totPeople += 1
    people.append(current[:])
    current.clear()

    answer = str(input('Wanna Continue? [S/N] ')).lower().strip()[0]

    while answer not in 'sn':
        answer = str(input('Please, choose a valid option! [S/N] '))


print(f'{len(people)} peoples wave been registered.')
print(f'{heavyList} are the heavest person with {heavy}Kg.')
print(f'{lightList} are the lightest person with {light}Kg')