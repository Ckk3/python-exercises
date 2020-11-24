# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

age = int(-1)
sex = str('v')
awnser = str('y').lower().strip()

contAgeUpperThanEighteen = int()
contMens = int()
contWomanYoungerThanTwent = int()

while awnser == 'y':

    age = -1
    sex = 'v'


    while sex not in 'mw':
        sex = str(input('Type the sex of the person [M/W]: ')).lower().strip()[0]
    while age < 1:
        age = int(input('Type the age : '))

    if age > 18:
        contAgeUpperThanEighteen += 1

    if sex == 'm':
        contMens += 1
    else:
        if age < 20:
            contWomanYoungerThanTwent += 1
    
    awnser = str(input('Want continue? [Y/N] '))


print(f'\n\nPeople oldest than 18 years: {contAgeUpperThanEighteen}\nTotal of mens: {contMens}\nWomans youngerst than 20 years: {contWomanYoungerThanTwent}')
    


    
    
