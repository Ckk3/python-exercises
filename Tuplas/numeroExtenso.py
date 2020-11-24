# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

txts = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fiveteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

answer = str('y')

while answer == 'y':
    number = int(input('Type a number between 0 and 20 to see in full: '))
    if 0 <= number <= 20:
        full = txts[number]
        print(f'{number} in full is {full}')
        answer = str(input('\nWanna type other number[Y/N]? ')).lower().strip()[0]

print('Bye!')