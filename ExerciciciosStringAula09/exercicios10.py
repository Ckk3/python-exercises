name = str(input('Type your entire name: ')).strip().lower()

search = str('silva') #Put in lower case

result = bool(search in name)

print('Your name has {}?\nAnswer: {}'.format(search, result))


