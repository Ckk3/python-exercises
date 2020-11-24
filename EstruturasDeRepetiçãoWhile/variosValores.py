# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

totalSum = int(0)
totalNum = int(0)

num = int(input('Type a number: '))

while num != 999:
    totalNum += 1
    totalSum += num
    num = int(input('Type other number (type 999 to stop): '))
    if num == 999:
        break

print(f'You typed {totalNum} numbers and de total sum is {totalSum}')