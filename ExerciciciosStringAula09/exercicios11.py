#Primeira e última ocorrência de uma string

text = str(input('Type a text: ')).lower().strip()

letter = str('a').lower()

print('The letter "{}" appear {} times in the text'.format(letter,text.count(letter)))
print('First time at {} position'.format(text.find(letter)+1))

print('Last time at {} position'.format(text.rfind(letter)+1))



