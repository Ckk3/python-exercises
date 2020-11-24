# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

'''
mass = float()
upper = float()
lower = float()

for p in range (0, 5):
    mass = float(input('Type the mass of the {}ª person: '.format(p + 1)))
    
    if p == 0:
        upper = mass
        lower = mass
    else:
        if mass > upper:
            upper = mass
        elif mass < lower:
            lower = mass

print('The upper value is {}Kg and the lower is {}Kg.'.format(upper, lower))
'''

lst = list([])

for p in range (0, 5):
    mass = float(input('Type the mass of the {}ª person: '.format(p + 1)))
    lst += [mass]
    
print('The upper value is {}Kg and the lower is {}Kg'.format(max(lst), min(lst)))







            

