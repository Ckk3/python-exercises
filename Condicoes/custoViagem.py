#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from time import sleep

tripDistance = float(input('Type the trip distance(KM): '))

#Variables
price = float(0)
shortTrips = float(0.50)
longTrips = float(0.45)
yOrN = ['Yes', 'No']


if tripDistance <= 200:
    price = tripDistance * shortTrips
    print('Distance is lower or equal than 200Km: {}\nR${:.2f}/km\nTotal: R${:.2f}'.format(yOrN[0], shortTrips, price))
else:
    price = tripDistance * longTrips
    print('Distance is lower or equal than 200Km: {}\nR${:.2f}/km\nTotal: R${:.2f}'.format(yOrN[1], longTrips, price))


