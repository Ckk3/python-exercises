# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

awnser = str('s')
values = list()
number = int()

while awnser == 's':

    number = int(input('Type a value: '))
    
    if number in values:
        print('Duplicate value, will be not added!')
    else:
        values.append(number)
        print('added value successfully!!')
    
    while True:
        awnser = str(input('Want to continue? [S/N] ')).lower().strip()[0]
        if awnser in 'sn':
            break

values.sort()
print('-=' * 15)
print(f'You typed the values: {values}')
print('-=' * 15)
