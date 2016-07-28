# Welcome to cipher day!
# write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers,
# symbols, and whitespace.
# for extra credit, add a "decrypt" function to your program!

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encrypt():
    message = input('Enter your secret message > ')
    key = int(input('Enter a number between 1 and 26 > '))
    cipher = ''

    for char in message:
        if char in ALPHABET:
            cipher += ALPHABET[(ALPHABET.index(char) + key) % (len(ALPHABET))]

    print('Your encrypted message is:',cipher)

encrypt()

# Limitations:
# 1. Uppercase chars not supported, results are n upper case fewer results e.g. 4 char string returns as 3
# 2. No check on int between 1 and 26.
# 3. No decryption
# 4. No int, or special character support
# 5. This is barebones.