from datetime import date

year = int(input('Digite que ano voce adquiriu seu carro: '))

userDate = date.today()
age =  userDate.year - year



if age<=3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')

print('Seu carro é novo!' if age<=3 else 'Seu carro é velho!')  