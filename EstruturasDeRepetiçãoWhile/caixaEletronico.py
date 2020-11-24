#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

withdraw = int(input('Withdraw value (Intenger): R$'))
total = withdraw

cont50 = int(0)
cont20 = int(0)
cont10 = int(0)
cont1 = int(0)

while total >= 50:
    total -= 50
    cont50 += 1

while total >= 20:
    total -= 20
    cont20 +=1

while total >= 10:
    total -= 10
    cont10 += 1

while total >= 1:
    total -= 1
    cont1 += 1


if cont50 > 0:
    print(f'\n{cont50} - R$50 banknotes', end='')
if cont20 > 0:
    print(f'\n{cont20} - R$20 banknotes', end='')
if cont10 > 0:
    print(f'\n{cont10} - R$10 banknotes', end='')
if cont1 > 0:
    print(f'\n{cont1} - R$1 banknotes', end='')



