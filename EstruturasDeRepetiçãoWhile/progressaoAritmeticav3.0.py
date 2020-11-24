# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

term = int(input('Type the first term of the AP: '))
reason = int(input('Type the reason: '))
number = term
final = int(10)
totalTerms = int(0)
#log = open('pa.txt', 'w')
cont = int(0)
while cont < final:    
    print('{}'.format(number), end='=>')
    #log.write('{}'.format(number))
    #log.write('=>')
    number += reason
    cont += 1
    totalTerms += 1
    if cont == final:
        print('Pause')
        final = int(input('how many terms do you want to show more?(Type 0 to stop) '))
        if final == 0:
            break
        cont = 0


print('The aritmetic progression was stoped with {} terms'.format(totalTerms))
#log.write('End!\nThe aritmetic progession was stoped with {} terms'.format(totalTerms))
#log.close()