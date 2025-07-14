import random

letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
char = '!@#$%^&*'

all_char = letter + num + char 

length = int(input('Enter the length of password.'))

password = ''

for i in range(length):
    password += random.choice(all_char)

print("The password is ",password)

