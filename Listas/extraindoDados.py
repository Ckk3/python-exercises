# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

values = list()
anwser = 's'


while anwser == 's':

    number = int(input('Type a value: '))
    values.append(number)
    
    while True:
        anwser = str(input('Wanna Continue? [S/N] ')).strip().lower()[0]
        if anwser in 'sn':
            break
        

values.sort(reverse=True)
print(values)

if 5 in values:
    print('The value 5 has in the list')
else:
    print('The value 5 hasnt in the list')


    