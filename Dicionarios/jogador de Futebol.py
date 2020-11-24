# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

player = dict()
goals = list()


player['name'] = str(input('Player name: '))
nMatches = int(input(f'Type how many matches {player["name"]} has played: '))

for c in range(0, nMatches):
    goalNumber = int(input(f'goals number in {c + 1} match: '))
    goals.append(goalNumber)


player['goals'] = goals
player['totalGoals'] = sum(goals)

print('-=' * 30)
print(player)

print('-=' * 30)
for key, value in player.items():
    print(f'The data {key} has value {value}')

print('-=' * 30)
print(f'The player {player["name"]} played {nMatches}')

for c in range(0, len(goals)):
    print(f'    => In {c + 1}ª match, scored {goals[c]} goals')

print(f'Has been a total of {player["totalGoals"]} goals')


