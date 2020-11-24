
galera = list()
dado = list()
totalMenor = totalMaior = int(0)

for c in range(0,4):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()



for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalMenor += 1

print(f'No total temos {totalMaior} maiores de idade e {totalMenor} menores de idade')