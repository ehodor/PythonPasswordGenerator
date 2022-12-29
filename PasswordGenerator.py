# Created by Emma Hodor on 12/29/2022

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Password Generator!')
print('Passwords should typically be at least 8 characters long with a mix of letters, numbers, and symbols '
      'to be safe.')

letter = int(input('How many letters would you like in your password?\n'))
number = int(input('How many numbers?\n'))
symbol = int(input('How many symbols?\n'))

password = random.choices(letters, k=letter) + random.choices(numbers, k=number) + random.choices(symbols, k=symbol)
random.shuffle(password)
password = ' '.join(password)
password = password.replace(" ", "")

print(f"Password is: {password}")
