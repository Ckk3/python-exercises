# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = int(0)

for c in range(1, 501, 2):
    if (c%3 == 0):
        print(c, end=' ')
        s += c
print('\n\n{}'.format(s))