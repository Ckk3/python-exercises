# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

contVi = int(0)
number = int(-1)
option = str('f')
pcNumber = randint(0, 10)

while True:
    
    number = int(input('Type a number: '))
    while number < 0:
        number = int(input('Type a number: '))
    
    option = str(input('Pair or Odd[P/O]: ')).strip().lower()
    while option not in 'po':
        option = str(input('Pair or Odd[P/O]: ')).strip().lower()[0]

    
    if option == 'p':
        if (number + pcNumber) % 2 == 0:
            contVi += 1
            print(f'The pc choose {pcNumber}, total is {pcNumber + number}\nYou Win!')
        else:
            break
    else:
        if (number + pcNumber) % 2 != 0:
            contVi += 1
            print(f'The pc choose {pcNumber}, total is {pcNumber + number}\nYou Win!')
        else:
            break

print(f'\nYou lose!!\nThe pc choose {pcNumber}.\nYou had {contVi} wins')
    


