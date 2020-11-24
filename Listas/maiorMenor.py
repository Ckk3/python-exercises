# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

values = list()

for cont in range(0, 5):
    values.append(int(input(f'Type the number for the {cont} position: ')))

maxValue = max(values)
minValue = min(values)



print(f'The max value is {maxValue} at position {values.index(maxValue)}')
print(f'The min value is {minValue} at position {values.index(minValue)}')
