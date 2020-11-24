'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

import os

firstNumber = int(input('Type the first number: '))
secondNumber = int(input('Type the first number: '))
option = int(0)
finalAnswer = str('')
while option != 5:
    option = int(input('What do you wanna do?\n[ 1 ] Sum\n[ 2 ] Multiply\n[ 3 ] Upper\n[ 4 ] New Numbers\n[ 5 ] Quit\nOption: '))

    if option == 1:
        finalAnswer = 'The sum of {} and {} is {}'.format(firstNumber, secondNumber, firstNumber + secondNumber)

    elif option == 2:
        finalAnswer = 'The multiply of {} and {} is {}'.format(firstNumber, secondNumber, firstNumber * secondNumber)

    elif option == 3:
        if firstNumber == secondNumber:
            finalAnswer = '{} and {} are equals!'.format(firstNumber, secondNumber)
        else:
            finalAnswer = '{} is upper than {}'.format(firstNumber if firstNumber > secondNumber else secondNumber, firstNumber if firstNumber < secondNumber else secondNumber)
    
    elif option == 4:
        firstNumber = int(input('Type the first number: '))
        secondNumber = int(input('Type the first number: '))
        finalAnswer = 'Now the numbers are {} and {}'.format(firstNumber, secondNumber)

    elif option == 5:
        break
    
    else:
        finalAnswer = 'Choose a valid option!!'
        
    os.system('cls')
    print(finalAnswer)
    os.system('pause')
    os.system('cls')

