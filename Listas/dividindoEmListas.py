# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

odds    = list()
pairs   = list()
values  = list()

while True:
    number = int(input('Type a number: '))

    values.append(number)
    if number % 2 == 0:
        pairs.append(number)
    else:
        odds.append(number)

    while True:
        anwser = str(input('Want to continue? [S/N] ')).lower().strip()[0]

        if anwser in 'sn':
            break
    
    if anwser == 'n':
        break


print('-=' * 30)
print(f'Total list: {values}')
print(f'Odds list: {odds}')
print(f'Pairs list: {pairs}')