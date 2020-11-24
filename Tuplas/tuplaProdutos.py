# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

products = ('Pencil', 'Eraser', 'Notebook', 'Case', 'Protractor', 'Compasses', 'Bag', 'Pens', 'Book')
prices = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)

print(f'\n{"PRODUCTS LIST":^40}')

for p in range(0, len(products)):
    print(f'{products[p]:.<30}', end='')
    print(f'R${prices[p]:>7.2f}')
