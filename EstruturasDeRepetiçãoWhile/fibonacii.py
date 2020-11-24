# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

quant = int(input('How many terms you wanna see? '))
previous = int(0)
actual = int(1)
cont = int(0)
res = int()
while cont < quant:
    if cont == 0:
        print('{}=>{}'.format(previous, actual), end='=>')
        cont += 2
    res = actual + previous
    print('{}'.format(res), end='=>')
    previous = actual
    actual = res
    cont += 1

print('End')
    