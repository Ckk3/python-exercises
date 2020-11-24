# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from datetime import date

currentYear     = date.today().year
olderName       = str()
ageList         = list([])
olderManAge     = int()
youngWoman      = int()

for c in range (0, 4):
    print('---- {}ª PERSON ----'.format(c + 1))
    name = str(input('Name: '))

    birthYear = int(input('BirthYear: '))
    age = currentYear - birthYear
    ageList += [age]

    sex = str(input('Sex [M/F]: ')).lower()
    if sex == 'm':
        if c == 0:
            olderName = name
            olderManAge = age
        else: 
            if age > olderManAge:
                olderManAge = age
                olderName = name
    elif sex == 'f':
        if age < 20:
            youngWoman += 1


print('The ages average is {} years'.format((ageList[0] + ageList[1] + ageList[2] + ageList[3])/4))
print('The oldest man has {} yeas and calls {}'.format(olderManAge, olderName))
print('In total, have {} woman{} with age lower than 20 years'.format(youngWoman, 's' if youngWoman > 1 else ''))
