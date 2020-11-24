# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint


numGames = int(input("How many games you want? "))
games = []

while numGames <= 0:
    print('Type a valid value!!')
    numGames = int(input("How many games you want? "))

print('-=' * 30)
print(' ' * 20 + f'SORTING {numGames} GAMES')
print('-=' * 30)


for c in range(0, numGames):

    games.append([])

    for j in range(0, 6):
        newNum = randint(0, 60)
        while newNum in games[c]:
            newNum = randint(0, 60)
        games[c].append(newNum)

    j = 0
    sleep(0.5)
    print(f'Game {c + 1}: {sorted(games[c])}')