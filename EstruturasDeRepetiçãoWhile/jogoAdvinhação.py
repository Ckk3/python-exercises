# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

secretNumber = int(randint(0, 10))
userTry = int()
tries = int()

userTry = int(input('Type your hunch: '))
tries += 1

while userTry != secretNumber:
    if userTry > secretNumber:
        print('Lower... Try again.')
    else:
        print('Upper... Try again.')
    
    tries +=1
    userTry = int(input('Type your hunch: '))

print('\nCongratulations!!\nYou hit after {} tries.'.format(tries))
