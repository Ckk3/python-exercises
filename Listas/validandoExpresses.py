# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = str(input('Type a valid expression with parentheses: '))
pilha = []

for char in expression:

    if char == '(':
        pilha.append('(')
    
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('The expression is valid!')
else:
    print('The expression isnt valid.')