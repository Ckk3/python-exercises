record1 = float(input('Insira a primeira nota do mês: '))
record2 = float(input('Insira a segunda nota do mês: '))

result = (record1 + record2) / 2

print('{:.2f}'.format(result))

if result >=6:
    print('O aluno passou!')
else:
    print('O aluno reprovou!')    
