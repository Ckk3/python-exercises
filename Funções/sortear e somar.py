# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def draw():
    for c in range(0, 5):
        numbers.append(randint(0, 999))
    print(f'The drawn numbers are {numbers}.')


def pairsSum(numbers):

    pairsList = list()
    for num in numbers:
        if num % 2 == 0:
            pairsList.append(num)
    print(f'The sum of the pairs numbers are {sum(pairsList)}')


numbers = list()
draw()
pairsSum(numbers)
