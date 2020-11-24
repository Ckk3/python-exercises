name = str(input('Type your name: ')).strip().lower()

if name == 'luis':
    print('Its a beatiful name!')
elif name == 'pedro' or name == 'joão' or name == 'maria':
    print('Your name is very popular in Brazil!')
elif name in 'cleiton':
    print('Your name is pika')
else:
    print('Your name is normal!')

print('Have a wonderful day!')    