#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number1 = int(input('Type the first number: '))
number2 = int(input('Type the second number: '))
number3 = int(input('Type the third number: '))

numberList = {number1, number2, number3}

numberList = sorted(numberList)

print('The upper number is {} and the lower number is {}'.format(numberList[2], numberList[0]))


'''
if number1 > number2 and number1 > number3:
    print('The upper number is {}'.format(number1))
else number2 > number1 and number2 >number3:
    print('The upper number is {}'.format(number2))
'''