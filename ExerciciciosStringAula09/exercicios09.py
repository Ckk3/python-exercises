name = str(input('Type your entire name: ')).strip()

print('Upper: {}'.format(name.upper()))
print('Tiny: {}'.format(name.lower()))

print('Letters number(entire name): {}'.format(len(name) - name.count(' ')))
#print('Letters number(first name): {}'.format(name.find(' ')))

part = name.split()

print('Your first name is "{}" and have {} letters'.format(part[0], len(part[0])))