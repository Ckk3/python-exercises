# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

names = []
notas = []
notasPos = 0
awnser = str('y')
studentNumber = int()

while awnser == "y":
    student = str(input('Type the student name: '))
    names.append(student)

    not1 = float(input('Type the first note: '))
    notas.append([])
    notas[notasPos].append(not1)
    not2 = float(input('Type the second note: '))
    notas[notasPos].append(not2)
    notasPos += 1

    awnser = str(input('Wanna continue? [Y/N]')).strip().lower()

    while awnser not in 'yn':
        awnser = str(input('Wanna continue? [Y/N]')).strip().lower()

for pos in range (0, len(names)):
    print(f'{pos} - {names[pos]}   | {(notas[pos][0] + notas[pos][1])/2}')


studentNumber = int(input('Type the number of the student to see their notes. [Type 999 to exit]'))
while studentNumber != 999:
    print(f"{names[studentNumber]}'s notes are {notas[studentNumber]} ")
    studentNumber = int(input('Type the number of the student to see their notes. [Type 999 to exit]'))