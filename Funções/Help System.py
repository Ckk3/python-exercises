# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.

from time import sleep
from colorama import Fore, Back, init, deinit

init()

def interactiveHelp(object):
    '''
    Search a help for any function or bibli in python
    :param object: function or bibli thats will de searched
    :return: the help() of the param object
    '''
    print(Back.WHITE,end='')
    print(Fore.BLACK,end='')
    help(object)
    print(Back.RESET, end='')
    print(Fore.RESET, end='')


def menu():
    '''
    shows the menu
    :return: print() with menu
    '''
    print(Back.BLUE, end='')
    print(Fore.WHITE, end='')
    print('-=' * 16)
    print('    INTERACTIVE HELP SYSTEM')
    print('-=' * 16)
    print(Back.RESET, end='')
    print(Fore.RESET, end='')


def searching(txt):
    print(Fore.WHITE, end='')
    print(Back.RED, end='')
    lenght = len(txt) + 33
    print('~' * lenght)
    print(f"   Accessing '{txt}' command manual")
    print('~' * lenght)
    print(Back.RESET, end='')
    print(Fore.RESET, end='')
    sleep(4)


while True:
    menu()
    trouble = str(input('Function or Bibli [999 to exit]: ')).strip().lower()

    if trouble == '999':
        break

    searching(trouble)
    interactiveHelp(trouble)




