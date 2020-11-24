# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

first = int(input('First term: '))
reason = int(input('Reason: '))

for c in range (0, 10):
    print(' {} '.format(first), end= '=>')
    first += reason
print(' End')