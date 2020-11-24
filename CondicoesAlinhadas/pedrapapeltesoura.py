# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
import random


print('''JOKEMPO
[ 1 ] for stone
[ 2 ] for paper
[ 3 ] for scissors''')

results = list(['Computer Wins', 'Player Wins', 'Tie'])
choices = list(['stone', 'paper', 'scissors'])

userChoice = int(input('Your option: '))
if userChoice <= 0 or userChoice > 3 :
    print('Select a valid option!')
    exit()
pcChoice = random.randint(1,3)

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!\n')
print('-=' * 11)
if userChoice == pcChoice:
    print(results[2])
    print('-=' * 11)
    print('The PC was choosed: {}\nThe Player was choosed: {}'.format(choices[pcChoice - 1], choices[userChoice - 1]))
elif userChoice == 1 and pcChoice == 2 or userChoice == 2 and pcChoice == 3 or userChoice == 3 and pcChoice == 1:
    print(results[0])
    print('-=' * 11)
    print('The PC was choosed: {}\nThe Player was choosed: {}'.format(choices[pcChoice - 1], choices[userChoice - 1]))
else:
    print(results[1])
    print('-=' * 11)
    print('The PC was choosed: {}\nThe Player was choosed: {}'.format(choices[pcChoice - 1], choices[userChoice - 1]))




