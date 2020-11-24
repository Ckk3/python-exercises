# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time do Flamengo.

teams = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco da Gama', 'Flamengo', 
        'Sport Recife', 'Santos', 'Fortaleza', 'Fluminense', 'Ceará SC', 'Grêmio', 'Corinthians', 'Atlético-Go', 
        'Athletico-PR', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Bahia', 'Goias')


print('First five teams:\n')

for pos in range(0, 5):
    print(f'{pos + 1} - {teams[pos]}')

print('\nLast four teams:\n')

for pos in range(16, 20):
    print(f'{pos + 1} - {teams[pos]}')

print('\nTeams in alphabetic order: \n')

for team in range(0, len(teams)):
    
    print(sorted(teams)[team])


print(f'\nFlamengo was in {teams.index("Flamengo") + 1} position')

