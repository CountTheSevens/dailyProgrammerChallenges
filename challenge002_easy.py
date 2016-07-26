# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
# Hello, coders! An important part of programming is being able to apply your programs, so your challenge for
# today is to create a calculator application that has use in your life. It might be an interest calculator,
# or it might be something that you can use in the classroom. For example, if you were in physics class,
# you might want to make a F = M * A calc.
# EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A,
# but also A = F/M, and M = F/A!

appTitle = 'PHYSICS CALCULATOR'

import math

def acceleration():
    f = input('What is your FORCE value? ')
    m = input('What is your MASS value? ')
    a = float(f) / float(m)
    print('Your ACCELERATION value is',a)
    

def force():
     m = input('What is your MASS value? ')
     a = input('What is your ACCELERATION value? ')
     f = float(m) * float(a)
     print('Your FORCE value is', f)


def mass():
     f = input('What is your FORCE value? ')
     a = input('What is your ACCELERATION value? ')
     m = float(f) / float(a)
     print('Your MASS value is', m)


def main():
    print(appTitle.center(32,'='),"\n")
    print('(1).....Calculate acceleration.')
    print('(2).....Calculate force.')
    print('(3).....Calculate mass.')
    print('(10)....Nope out of this!\n')
    print('='.center(32,'='))
    calcMode = input('I want to...:')

    if calcMode == '1':
        acceleration()
    if calcMode == '2':
        force()
    if calcMode == '3':
        mass()
    else:
        quit()

main()
