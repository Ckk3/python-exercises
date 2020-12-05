# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def scores(*notes, situation=False):
    '''
    Fuction to analise scores and situations of students
    :param notes: Get notes
    :param situation: See the final situation
    :return: dict() with total, upper score, lower score, average and situation(if True)
    '''

    results = dict()
    results['total'] = len(notes)
    results['upper'] = max(notes)
    results['lower'] = min(notes)
    average = float(sum(notes)/len(notes))
    results['average'] = average

    if situation:
        if average < 6:
            results['Situation'] = 'BAD'
        elif average < 8:
            results['Situation'] = 'OK'
        elif average <= 10:
            results['Situation'] = 'VERY GOOD'
        else:
            print('ERROR')

    return results


anwser = scores(9.32, 2, 5, 9.43, 2, 7 ,5.3, 3.7, 1.32, situation=True)
print(anwser)