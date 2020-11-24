# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

people = list()
womans = list()
aboveAvg = list()

register = dict()
awnser = str('y')
totAge = int(0)
totWoman = int(0)


while awnser != 'n':
    register['name'] = str(input('Name: '))

    while True:
        register['sex'] = str(input('Sex[W/M]: ')).strip().lower()

        if register['sex'] not in 'mw':
            print('Please, choose a valid option!')
        else:
            if register['sex'] == 'w':
                womans.append(register['name'])
            break

    register['age'] = int(input('Age: '))
    totAge += register['age']

    people.append(register.copy())
    register.clear()
    while True:
        awnser = str(input('Wanna Continue? [Y/N] ')).strip().lower()

        if awnser not in 'yn':
            print('Please, choose a valid option!')
        else:
            break


totPeople = len(people)
average = float(totAge/totPeople)

for person in people:
    if person['age'] > average:
        aboveAvg.append(person['name'])

print('=+' * 30)
print(f'Altogether, {totPeople} were registered')
print(f'The age average is {average}')
print(f'The womans registered: ')

for woman in womans:
    print(f'{woman} ', end=' ')


print(f'\nPeople above age average: ')

for above in aboveAvg:
    print(f'{above} ', end=' ')


