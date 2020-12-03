# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def factoriaL(n, show=False):
    '''
    Calculate the factorial
    :param n: number whos factorial will be calculate
    :param show: bollean thats will show or not the calcules
    :return: result of the factorial
    '''
    f = 1
    for c in range(n, 0, -1):
        f *= c

        if show:
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end='*')

    print(f'{f}')


num = int(input('Type the number you want see the factorial: '))

trueOrFalse = int(input('Wanna see the calculations? [0 = NO, 1 = TRUE] '))
while 1 != trueOrFalse != 0:
    trueOrFalse = int(input('Wanna see the calculations? [0 = NO, 1 = TRUE] '))

if trueOrFalse == 1:
    trueOrFalse = True
elif trueOrFalse ==0:
    trueOrFalse = False
else:
    print('Uncommom error, pls restart')


factoriaL(num, show=trueOrFalse)


