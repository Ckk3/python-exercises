# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numbers = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100) )

print('The sorteds values are:', end='')
for n in numbers:
    print(f' {n}', end='')
print('.')
print(f'\nLower: {min(numbers)}\nUpper: {max(numbers)}')



    
