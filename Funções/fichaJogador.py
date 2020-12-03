# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def token(name = '<unknow>', goals = str(0)):
    if not goals.isnumeric():
        goals = 0

    if len(name) == 0:
        name = '<unknow>'

    print(f'The player {name} scored {goals} goal(s) in the championship.')


playerName = str(input('Player name: ')).strip()
playerGoals = str(input('Goals scored: '))

token(name=playerName, goals=playerGoals)