# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def counter(start, end, step):
    print(f'Counting from {start} to {end} in {step} in {step}')
    
    if end < start and step > 0:
        step = -step

    if end < 0:
        end -= 1
    elif end > 0:
        end += 1
    elif end == 0:
        end = -1

    for c in range(start, end, step):
        print(f'{c}', end=' ')
        sleep(0.3)
    print('END\n')


counter(1, 10, 1)
counter(10, 0, 2)
counter(12, -10, 7)