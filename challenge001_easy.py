#https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
# #create a program that will ask the users name, age, and reddit username. have it tell them the information back,
#in the format: your name is (blank), you are (blank) years old, and your username is (blank)
#for extra credit, have the program log this information in a file to be accessed later.

name = input("What is your name? ")
age = input("How old are you? ")

if age is not int:
    age = input("Please enter a numeric value for your age. ")

redditName = input("What's your Reddit username? ")
f = open('challenge001_easy_output.txt', 'a')

print('Your name is', name,', you\'re', age, 'years old, and your Reddit username is', redditName, '.')

out = name,age, redditName

f.write(str(out))
f.write('\n')
f.close()

