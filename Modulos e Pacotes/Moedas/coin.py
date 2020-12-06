import operations

price = float(input('Price: R$ '))
tax = float(input('Tax (%):'))

increasedPrice = operations.increase(price, tax)
decreasedPrice = operations.decrease(price, tax)
doublePrice = operations.double(price)
halfPrice = operations.half(price)


print(f'Incresing {tax}%, we have {increasedPrice}')
print(f'Incresing {tax}%, we have {decreasedPrice}')
print(f'The double of {price} is {doublePrice}')
print(f'The half of {price} is {halfPrice}')
