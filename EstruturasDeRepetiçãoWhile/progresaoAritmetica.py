# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

term = int(input('Type the first term of the AP: '))
reason = int(input('Type the reason: '))
number = term

cont = int(0)
while cont < 10:    
    print('{}'.format(number), end='=>')
    number += reason
    cont += 1

print('FIM')