#dados = {'nome': 'Luis Gustavo', 'idade': 17, 'sexo': 'M'}
#teste = []

#teste.append(dados)
#print(dados.values())
#print(dados.keys())
#print(dados.items())
#print(dados)
#print(teste)
#print(teste[0]['nome'])

#for key, value in dados.items():
    #print(f'The {key} is {value}')

brazil = list()
state = dict()

for c in range(0, 3):
    state['uf'] = str(input('Type the state name: '))
    state['initials'] = str(input('Type the initials: '))
    state['capital'] = str(input('Type the capital: '))

    brazil.append(state.copy())


print(brazil)