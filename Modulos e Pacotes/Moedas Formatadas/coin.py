import formatedOperations

price = float(input('Price: R$ '))
tax = float(input('Tax (%):'))

increasedPrice = formatedOperations.increase(price, tax)
decreasedPrice = formatedOperations.decrease(price, tax)
doublePrice = formatedOperations.double(price)
halfPrice = formatedOperations.half(price)


print(f'Incresing {tax}%, we have {formatedOperations.formatPrice(increasedPrice)}')
print(f'Decreasing {tax}%, we have {formatedOperations.formatPrice(decreasedPrice)}')
print(f'The double of {price} is {formatedOperations.formatPrice(doublePrice)}')
print(f'The half of {price} is {formatedOperations.formatPrice(halfPrice)}')
