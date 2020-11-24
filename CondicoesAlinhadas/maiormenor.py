# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

number1 = int(input('Type the first number: '))
number2 = int(input('Type the second number: '))

if number1 > number2:
    print('The first number is upper!')
elif number2 > number1:
    print('The second number is upper!')
else:
    print('The numbers are equals!')    