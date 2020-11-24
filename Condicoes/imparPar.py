#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from time import sleep

number = int(input('Type a number: '))

print('Loading...')
sleep(1)

if (number % 2) == 0:
    print('The number {} is even!'.format(number))
else: 
    print('The Number {} is odd!'.format(number))