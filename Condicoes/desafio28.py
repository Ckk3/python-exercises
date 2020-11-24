#Faça o computador pensar em um número interio entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá excrever na tela e o usuário ganhou ou perdeu!

from random import randint
from time import sleep

print('I will think a ramdom name from 0-5. Try to guess...\n')
number = int(input('What number did i think of? '))

anwser = randint(0,5)
sleepTime = 1

print('LOADING...\n')
sleep(sleepTime)
if number==anwser:
    print('Wow, you win!')
else:
    print('You lose, i Win!')


