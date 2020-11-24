#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from colorama import Fore

number = int(input('Type a intenger number: '))
divisions = int(0)
for c in range(1, number + 1):
    if (number % c) == 0:
        divisions += 1
        print(Fore.CYAN + '{}'.format(c), end=' ')
    else:
        print(Fore.YELLOW + '{}'.format(c), end=' ')

print(Fore.RESET)
if divisions == 2:
    print('The number {} is cousin!!'.format(number))
else:
    print('The number {} isnt cousin!'.format(number))