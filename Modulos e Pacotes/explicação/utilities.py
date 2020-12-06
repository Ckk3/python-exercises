
def specialPrint(txt):
    length = len(txt) + 6
    print(f'~' * length)
    print(f'   {txt}')
    print(f'~' * length)

    return



def factoriaL(n, show=False):
    '''
    Calculate the factorial
    :param n: number whos factorial will be calculate
    :param show: bollean thats will show or not the calcules
    :return: result of the factorial
    '''
    f = 1
    for c in range(n, 0, -1):
        f *= c

        if show:
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end='*')

    return f
