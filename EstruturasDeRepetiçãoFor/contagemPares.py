# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

end = int(input('End: '))

for c in range(1,end+1, +1):
    if(c%2 == 0):
        print(c)
