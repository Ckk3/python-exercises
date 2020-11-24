'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date



categories = list(['Little','Childish', 'Junior', 'Senior', 'Master'])


birthYear = int(input('Type your birth year: '))

currentYear = int(date.today().year)
age = int(currentYear - birthYear)

print('The athlete has {} years old'.format(age))

if age <= 9:
    print('Category: {}'.format(categories[0]))
elif age <= 14:
    print('Category: {}'.format(categories[1]))
elif age <= 19:
    print('Category: {}'.format(categories[2]))
elif age <= 25:
    print('Category: {}'.format(categories[3]))
else:
    print('Category: {}'.format(categories[4]))