# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

currentYear = int(datetime.now().year)

worker = dict()

worker['name'] = str(input('Name: '))
birthYear = int(input('Bith year: '))
worker['age'] = int(currentYear - birthYear)
worker['ctps'] = int(input('Your ctps number [type 0 dont have]: '))

if worker['ctps'] != 0:
    worker['contractYear'] = int(input('Contract Year: '))
    worker['salary'] = float(input('Salary value: R$'))
    worker['retirement'] =  int((currentYear - worker['contractYear']) + 35 + worker['age'])

print('+=' * 30)

for key, value in worker.items():
    print(f'{key} has value {value}')

print('+=' * 30)
