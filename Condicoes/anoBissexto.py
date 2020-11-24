#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
import calendar

year = int(input('What year do you want verify? Insert "0" if you want the current year: '))
currentYear = date.today().year

if year == 0:
    year = currentYear

'''  
if (year % 4) == 0 and (year % 100) == 0 or year:
    print('{} is bissextile!'.format(year))
else:
    print('{} isnt bissextile!'.format(year))
'''

if calendar.isleap(year):
    print('{} is bissextile!'.format(year))
else:
    print('{} isnt bissextile!'.format(year))