# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

game = dict()


for c in range(0, 4):
    name = str(input(f'Name of the {c + 1} player: '))
    game[f'{name}'] = randint(1, 6)

ranking = dict(sorted(game.items(), key= itemgetter(1), reverse= True))


print(f'=-' * 20)

pos = int(0)
for k, v in ranking.items():
    pos += 1
    print(f'{pos}º place --> {k} =- {v}')
del(pos)



