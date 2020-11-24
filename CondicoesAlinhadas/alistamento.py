# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

birthYear = int(input('Type your bithYear: '))

currentYear = int(date.today().year)

age = currentYear - birthYear

if age == 18:
    print('You are just in time to enlist!')
elif age < 18:
    print('You still wait {} years to do your enlistment.\nOnly in {}'.format(18 - age , (18 - age) + currentYear))
else:
    print('You should have done your enlist in {}!\nNow you are {} years late!'.format(currentYear - (age - 18), (age - 18)))