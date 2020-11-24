# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

from datetime import datetime
from time import sleep

print('DETRAN SEARCH')
maxSpeed = float(input('Type the max speed of the road: '))
currentSpeed = float(input('Type the car speed: '))
sleepTime = 1
mulctPrice = float(0)


print('\nLoading...\n')
sleep(sleepTime)

if currentSpeed > maxSpeed:
    mulctPrice = (currentSpeed - maxSpeed) * 7
    print('You will be mulct!\nValor: R${:.2f}\n\nConsult time: {}'.format(mulctPrice,datetime.now()))
else:
    print('You dont will be mulct!\n\nConsult time: {}'.format(datetime.today()))