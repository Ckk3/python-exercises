# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

situation = dict()

situation['name'] = str(input('Name: '))
situation['mean'] = float(input('Mean: '))

if situation['mean'] >= 7:
    situation['situation'] = str('Aproved!')
elif situation['mean'] >= 6:
    situation['situation'] = str('Recuperation!')
else:
    situation['situation'] = str('Disaproved!!')

for k, v in situation.items():
    print(f'{k} -> {v}')
