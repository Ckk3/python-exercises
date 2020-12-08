'''
Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
'''

import datas as formatedOperations

price = formatedOperations.readMoney('Price: R$ ')
tax = formatedOperations.readMoney('Tax (%): ')

increasedPrice = formatedOperations.increase(price, tax)
decreasedPrice = formatedOperations.decrease(price, tax)
doublePrice = formatedOperations.double(price)
halfPrice = formatedOperations.half(price)


print(f'Incresing {tax}%, we have {formatedOperations.formatPrice(increasedPrice)}')
print(f'Decreasing {tax}%, we have {formatedOperations.formatPrice(decreasedPrice)}')
print(f'The double of R${price} is {formatedOperations.formatPrice(doublePrice)}')
print(f'The half of R${price} is {formatedOperations.formatPrice(halfPrice)}')
