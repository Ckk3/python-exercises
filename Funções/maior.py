# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def upper(* numbers):
    print(f'The upper number is {numbers[0][0]}')


quant = int(input('how many numbers you want add? '))
numbersList = list()
for c in range(1, quant + 1):
    numbersList.append(int(input(f'Type the {c} number: ')))



numbersList.sort(reverse= True)
upper(numbersList)