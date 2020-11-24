# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
from colorama import Fore

currentYear = date.today().year
minors = int(0)
olders = int(0)


for people in range (0, 7):
    birthYear = int(input('Type the Birth Year of the {}ª person: '.format(people + 1))) 
    if (currentYear - birthYear) > 17:
        olders += 1
    else:
        minors += 1

print('In total, has {}{}{} older{} and {}{}{} minor{}.'.format(Fore.CYAN, olders, Fore.RESET , 's' if olders > 1 else '', Fore.GREEN ,minors, Fore.RESET,  's' if minors > 1 else ''))
