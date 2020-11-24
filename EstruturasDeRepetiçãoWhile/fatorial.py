#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from time import sleep
from math import factorial

userNum = int(input('Type the number who you want to know the factorial: '))


print('Calculating.',end='')
sleep(0.3)
print('.',end='')
sleep(0.3)
print('.')
sleep(0.3)

#Using While
'''
num = int(userNum)
fat = int(userNum - 1)
res = int(0)
finalRes = int(1)
while fat > 0:
    res = fat * num

    finalRes *= res
    fat -= 2
    num -= 2

print('!{} = {}'.format(userNum, finalRes))
'''

#Using for
'''
num = int(userNum)
fat = int(userNum - 1)
res = int(0)
finalRes = int(1)

for fat in range (userNum - 1, 0, -2):
    res = fat * num
    finalRes *= res
    num -= 2

print('!{} = {}'.format(userNum, finalRes))
'''

#Using factorial class
'''
print('!{} = {}'.format(userNum, factorial(userNum)))
'''

