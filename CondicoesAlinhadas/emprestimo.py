# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

totalValue = float(input('Type the total value of the house: '))
wage = float(input('Type the salary of the purchaser: '))
years = int(input('Type the total of years: '))
months = int(years*12)
mensalValue = float(totalValue/months)

wagePercentage = float(wage*0.3)

if mensalValue > wagePercentage:
    print('\nThe lending was DENIED!')
else:
    print('\nThe lending was been accept!\nMonthly installments: R${:.2f}\nTotal months: {}'.format(mensalValue, months))