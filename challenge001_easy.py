#create a program that will ask the users name, age, and reddit username. have it tell them the information back,
#in the format:
#
#your name is (blank), you are (blank) years old, and your username is (blank)
#
#for extra credit, have the program log this information in a file to be accessed later.
#
import csv

name = input("What is you name? ")
age = input("How old are you? ")
redditName = input("What's your Reddit username? ")
f = open('challenge001_easy_output.txt', 'a')

print('Your name is', name, ', you\'re', age, 'years old, and your Reddit username is', redditName, '.')
out = name,age,redditName
printLine = str(out)


f.write(printLine)
f.write('\n')
f.close()

# Ideas
# 1. Check input format, e.g. age is an int
# 2. Change out to a dictionary {name: age, redditName}