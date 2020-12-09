
try:
    num = int(input('Numerator: '))
    dem = int(input('Denominator: '))
    res = num/dem

except (TypeError, ValueError):
    print('We have a problem with the inserted types')

except ZeroDivisionError:
    print('Division by Zero is invalid!!!')

except Exception as error:
    print(f'We have a inespect error: {error.__class__}')

else:
    print(f'The result of {num}/{dem} is {res}')