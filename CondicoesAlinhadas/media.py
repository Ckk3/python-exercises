# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


firstNote = float(input('Type the first note: '))
secondNote = float(input('Type the second note: '))

average = float((firstNote + secondNote)/2)

if average < 5:
    print('The student average was {:.2f}, he/she will be reproved!!'.format(average))
elif average < 7:
    print('The student average was {:.2f}, he/she will make the recovery!'.format(average))
elif average <= 10:
    print('The student average was {:.2f}, he/she was aproved!!'.format(average))