# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

lower = int(0)
upper = int(0)
average = float(0)
awnser = str('')

cont = int(0)
totSum = int(0)

while awnser != 'n':
    firstNumber = int(input('Type a number: '))
    cont += 1

    if cont == 1:
        upper = lower = firstNumber

    if firstNumber < lower:
        lower = firstNumber
    elif firstNumber > upper:
        upper = firstNumber

    totSum += firstNumber
    average =  float(totSum / cont)
    
    awnser = str(input('Wanna continue? [S/N] ')).lower().strip()
    
    
print('You typed {} numbers and de average is {}\nThe upper value is {} and the lower {}'.format(cont, average, upper, lower))
