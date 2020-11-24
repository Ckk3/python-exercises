# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

values = (int(input('Type the first value: ')), 
            int(input('Type the second value: ')), 
            int(input('Type the third value: ')), 
            int(input('Type the fourth value: ')))

cont = int(0)

print(f'You typed the values {values}')

print(f'\nYou typed "9" {values.count(9)} times')

if 3 in values:
    print(f'The value "3" apper in position {values.index(3) + 1}')
else: 
    print('The value "3" has not typed')

for v in values:
    if v % 2 == 0 and cont == 0:
        print('The pair numbers you has typed are {}'.format(v), end='')
        cont += 1
    elif v % 2 == 0:
        print(f' {v}')
    
        
    

