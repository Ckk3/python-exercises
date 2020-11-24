
snack = ('Hamburger', 'Suco', 'Pizza','Pudim')

for food in snack:
    print(food)

print('')
for cont in range(0, len(snack)):
    print(snack[cont])

print('')

for pos, food in enumerate(snack):
    print(f'{food} in position {pos}')

print(sorted(snack))

del(snack)