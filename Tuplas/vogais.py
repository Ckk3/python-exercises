# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.



words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
        'trabalhar', 'mercado', 'programador', 'futuro')

for w in words:
    print(f'In {w.upper()} we have ', end='')    
    
    for l in w:
        if l.lower() in 'aeiou':
            print(f'{l}', end=' ')
    

    print('')
        

