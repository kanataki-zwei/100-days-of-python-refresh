# password generator
import string
import random
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
numbers = list(string.digits)  
symbols = list('!@#$%^&*()-_=+[]{};:,.<>?/~`|')

upper_letters = int(input("How many uppercase letters do you want?: "))
lower_letters = int(input("How many lowercase letters do you want?: "))
digits = int(input("How many digits do you want?: "))
special_symbols = int(input("How many symbols do you want?: "))

password = []
for char in range(upper_letters):
    password.append(random.choice(uppercase_letters))

for char in range(lower_letters):
    password.append(random.choice(lowercase_letters))

for char in range(digits):
    password.append(random.choice(numbers))

for char in range(special_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
password = ''.join(password)
print(password)