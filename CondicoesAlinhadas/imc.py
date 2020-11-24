'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

#IMC = peso/(altura^2)

imcType = list(['Under weight', 'Ideal weight', 'Overweight', 'Obesity', 'Morbid obesity'])

weight = float(input('Type your weight(Kg): '))
height = float(input('Type your height(m): '))

imc = weight / (height * height)

if imc < 18.5:
    print('Your imc is {:.2f}({})'.format(imc , imcType[0]))
elif imc < 25:
    print('Your imc is {:.2f}({})'.format(imc , imcType[1]))
elif imc < 30:
    print('Your imc is {:.2f}({})'.format(imc , imcType[2]))
elif imc < 40:
    print('Your imc is {:.2f}({})'.format(imc , imcType[3]))
else:
    print('Your imc is {:.2f}({})'.format(imc , imcType[4]))     