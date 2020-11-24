# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

number = int(input('Type a number to see your multiplication table: '))

for c in range (1, 11):
    print('{} x {:2} = {}'.format(number, c, (number * c)))