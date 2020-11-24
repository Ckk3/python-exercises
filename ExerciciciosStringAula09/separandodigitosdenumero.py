number = int(input('Insert a intenger number: '))
print('Analyzing the number "{}"'.format(number))

unit = number//1 % 10
dicker = number//10 % 10
hundred = number//100 % 10
thousand = number//1000 % 10

print('Unit: {}'.format(unit))
print('Dicker: {}'.format(dicker))
print('Hundred: {}'.format(hundred))
print('Thousand: {}'.format(thousand))