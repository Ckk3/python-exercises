# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

productName         = str('')
cheapProductName    = str('')
price               = float()
lowerPrice          = float(0)
totalPrice          = float()
contProductPrice    = int()
awnser              = str('y').lower()
cont                = int(0)

while awnser == 'y':

    price = 0
    awnser = str('b')


    productName = input('Product name: ')

    while price <= 0:
        price = float(input('Product price: '))
    
    totalPrice += price

    if price > 1000:
        contProductPrice += 1
    
    if cont == 0:
        lowerPrice = price
        cheapProductName = productName
    else:
        if price < lowerPrice:
            lowerPrice = price
            cheapProductName = productName

    cont +=1

    while awnser not in 'yn':
        awnser = input('Want continue? [Y/N] ').lower().strip()[0]


print(f'\n\nTotal: R${totalPrice:.2f}\nWas {contProductPrice} products costing over than R$1000.00\nThe cheapest product is the {cheapProductName} costing R${lowerPrice:.2f}')

    

    