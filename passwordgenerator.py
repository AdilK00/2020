import random

print('''
Wachtwoord Generator
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('Number of passwords?')
number = int(number)

length = input('Password length?')
length = int(length)

print('Here are your passwords:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)