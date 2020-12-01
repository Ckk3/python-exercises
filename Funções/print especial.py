# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~~


def specialPrint(txt):
    length = len(txt) + 6
    print(f'~' * length)
    print(f'   {txt}')
    print(f'~' * length)

specialPrint('Luis Gustavo')
specialPrint('Ifma')
specialPrint('Flamengo 2 x 0 River Plate gol do Gabigol')