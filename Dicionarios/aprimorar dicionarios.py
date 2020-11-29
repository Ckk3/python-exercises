# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

listPlayer = list()
player = dict()
goals = list()
awnser = str()
playerNum = int()

while True:
    player['name'] = str(input('Player name: '))
    nMatches = int(input(f'Type how many matches {player["name"]} has played: '))

    goals.clear()
    for c in range(0, nMatches):
        goalNumber = int(input(f'goals number in {c + 1} match: '))
        goals.append(goalNumber)


    player['goals'] = goals[:]
    player['totalGoals'] = sum(goals)

    listPlayer.append(player.copy())

    awnser = 'k'
    while awnser not in 'yn':
        awnser = str(input("Wanna Continue? [Y/N]")).strip().lower()

        if awnser not in 'yn':
            print('Choose a Valid option!!')


    if awnser == 'n':
        break


print('-=' * 30)

print('Nº | name           | Goals       |Total')
print('-' * 25)
for c in range(0, len(listPlayer)):

    print(f'{c:<4}',end='')
    print(f'{listPlayer[c]["name"]:<17}', end='')
    print(f'{str(listPlayer[c]["goals"]):<15}', end='')
    print(f'{listPlayer[c]["totalGoals"]:<15}', end='')
    print()

print('-=' * 30)

while True:

    playerNum = -1

    playerNum = int(input('Choose a player by his number: (Type 999 to stop) '))

    if playerNum == 999:
        break
    elif playerNum > (len(listPlayer) - 1) or playerNum < 0:
        print('Type a valid number!!')
    else:
        print(f'  --{listPlayer[playerNum]["name"]} STATS')

        for c in range(0, len(listPlayer[playerNum]['goals'])):
            print(f'Game {c + 1} scored {listPlayer[playerNum]["goals"][c]} goals')
