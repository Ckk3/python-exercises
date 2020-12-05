# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def readInteger(txt=str()):

    strNum = str(input(txt))

    if strNum.isnumeric():
        num = int(strNum)
        return num
    else:
        while not strNum.isnumeric():
            strNum = str(input('ERROR! Type a valid integer number.\nNumber: '))
        num = int(strNum)
        return num


number = readInteger('Type a number: ')
print(f'The writed number is {number}')

