# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input('Type a intenger number: '))

print('''\nChoose one of thats bases do covert:
[ 1 ] convert to BINARY
[ 2 ] convert to OCTAL
[ 3 ] convert to HEXADECIMAL''')

option = int(input('Option: '))

if option == 1:
    print('{} in binary is {}'.format(number, bin(number)))
elif option == 2:
    print('{} in octal is {}'.format(number, oct(number)))
elif option == 3:
    print('{} in hexadecimal is {}'.format(number, hex(number)))
else:
    print('Choose a valid option!')    