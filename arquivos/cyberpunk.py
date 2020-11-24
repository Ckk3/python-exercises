

name = str(input('Type your name: '))
bithYear = int(input('Type you BithYear: '))
gender = str(input('Type your gender: '))


arquivo = open('dados.txt', 'w')
arquivo.write('{}\n{}\n{}\n'.format(name,bithYear,gender,))
arquivo.close()


arquivo = open('dados.txt','r')

txtName = str(arquivo.readline())
txtBithYear = int(arquivo.readline())
txtGender = str(arquivo.readline())

print('\n\nYour name: {}Your bithYear: {}\nYour gender: {}'.format(txtName, txtBithYear, txtGender))
