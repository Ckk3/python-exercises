
def soma(* num):
    print(sum(num))


def title(txt):
    print('-=' * 10)
    print(txt)
    print('-=' * 10)


def double(numbers):
    pos = 0
    while pos < len(numbers):
        numbers[pos] *= 2
        pos += 1
    print(numbers)


title('Dobrar')
values = [6, 3, 9, 1, 0, 2]
double(values)
title('Soma')
soma(5, 7, 10, 23, 12)

