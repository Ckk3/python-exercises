# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

n1 = int(input('Type any intenger number: '))
n2 = int(input('Type any intenger number: '))
n3 = int(input('Type any intenger number: '))
n4 = int(input('Type any intenger number: '))
n5 = int(input('Type any intenger number: '))
n6 = int(input('Type any intenger number: '))

numbers = list([n1,n2,n3,n4,n5,n6])
sum = int(0)

for c in range(0,6):
    currentNumber = numbers[c]
    if (currentNumber % 2 == 0):
        sum += currentNumber
    
print('The summation of the pairs numbers is: {}'.format(sum))
