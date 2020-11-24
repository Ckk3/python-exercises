#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

text = str(input('Type a text: ').strip().lower())

listTextCount = text.split()

lText = str('' .join(listTextCount))
rText = str('')


for i in range (len(lText) - 1, -1, -1):
    rText = rText + lText[i]


if lText == rText:
    print('Is a palindrome!')
else:
    print('Isnt a palindrome.')