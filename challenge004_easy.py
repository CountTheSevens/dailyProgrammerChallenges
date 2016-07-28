# You're challenge for today is to create a random password generator!
# For extra credit, allow the user to specify the amount of passwords to generate.
# For even more extra credit, allow the user to specify the length of the strings he wants to generate!

import random

STRING_LIST = 'abcdefghijklmnopqrstuvwxyz'
SPEC_CHAR_LIST = '!@#$%^&*()?.'
NUM_LIST = '0123456789'

def main():
    print('Ub3r h@x0r p@$$w0rd G3n3rat0r!'.center(50, '-'))
    pwLen = int(input('How many characters do you want the password to be? >> '))
    pwSpec = input('Do you want special characters? (yes/no) >> ')
    pwNum = input('Do you want numbers? (yes/no) >> ')

    if pwSpec == 'yes':
        pwSpec = 1
    else:
        pwSpec = 0

    if pwNum == 'yes':
        pwNum = 1
    else:
        pwNum = 0

    passwordGenerator(pwLen, pwSpec, pwNum)


def passwordGenerator(len, spec, num): # Length, special characters, numbers options 1=y 2=n
    print('made it to pw def')
    print(len, spec, num)

main()