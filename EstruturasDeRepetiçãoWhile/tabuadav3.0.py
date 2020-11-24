# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo. 
from os import system

number = int(input('Type a number to see the table: '))


while number > -1:

    for c in range(1,11):
        print(f'{number} x {c} = {number * c}')
    
    number = int(input('Type other number(negative number to end):'))
    system('cls')

system('cls')
print('Multiplication table finished!!')
