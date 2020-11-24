#Primeiro e último nome de uma pessoa

name = str(input('Type your name: ')).strip()
listName = name.split()

print('Your first name is: {}'.format(listName[0]))
print('Your last name is: {}'.format(listName[len(listName)-1]))
