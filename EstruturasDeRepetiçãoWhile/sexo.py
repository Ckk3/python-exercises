# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

answer = str('f')
verify = str('d')

answer = str(input('Type your sex [M/W]: ')).lower().strip()

while answer not in 'mw':
    print('Type a valid sex!!')
    answer = str(input('Type your sex [M/W]: ')).lower().strip()

print('You selected {}'.format(answer))