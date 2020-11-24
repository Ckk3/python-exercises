'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''


productPrice            = float(input('Type the product price: R$'))
answer                  = int(input('Select a payment option:\n[1]In Cash/check;\n[2]1x in card;\n[3]2x in card;\n[4]3x or more in card.\nAnswer: '))
instalmentPrice         = float(0)
finalProductPrice       = float(0)

if answer == 1:
    finalProductPrice   = productPrice * 0.9
    print('Option choosed: pay with cash.\nYou received 10% off so the final price is R${:.2f}'.format(finalProductPrice))
elif answer == 2:
    finalProductPrice   = productPrice * 0.95
    print('Option choosed: 1x in card.\nYou received 5% off so the final price is R${:.2f}'.format(finalProductPrice))
elif answer == 3:
    finalProductPrice   = productPrice
    print('Option choosed: 2x in card.\nThe final price is R${:.2f}'.format(finalProductPrice))
elif answer == 4:
    instalmentNumbers   = int(input('Type the numbers of instalments: '))
    interestTax         = float(0.2)
    interest            = productPrice * interestTax
    finalProductPrice   = productPrice + interest
    instalmentsPrice    = finalProductPrice/instalmentNumbers
    print('Option choosed: 3x or more in card.\nYou will pay {} instalments of R${:.2f} and the final price is R${:.2f}'.format(instalmentNumbers , instalmentsPrice , finalProductPrice))




