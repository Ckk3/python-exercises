# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def vote(year):
    '''
    :param year: Bith year of the person
    :return: the person vote status (DENIED, OPTIONAL, MANDATORY)
    '''
    from datetime import date
    global age
    age = int(int(date.today().year) - year)

    if age < 16:
        return 'DENIED'
    elif age < 18:
        return 'OPTIONAL'
    else:
        return 'MANDATORY'


birthYear = int(input('Type your birth year: '))
situation = vote(birthYear)

print(f'You {age} years old and your vote situation is {situation}')