c = int(4)
a = str('y')
pair = int(0)
odd = int(0)

while a == 'y':
    c = int(input('Type a number: '))
    a = str(input('Want to continue [Y/N]')).lower()
    if c % 2 == 0:
        pair += 1
    else:
        odd += 1
print('You typed {} odd numbers and {} pairs'.format(odd, pair))