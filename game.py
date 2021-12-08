"""A number-guessing game."""

import random
# from random import function_name

print("Greetings Player! Enter below your preferred name:")

name = input()
# print(name)
print("Welcome",name,"\nI'm thinking of a number between 1-100. Think you can guess it right on the first try?")

random_num = random.randint(1,10)
# print(random_num)

guess = True
num_guess = 0
while guess:
    try:
        guess = int(input())
    except:
        guess = True
        print('To reiterate, a NUMBER between 1-100. You should only be entering integers.')
    num_guess += 1
    if guess < 0 or guess > 100:
        print('Hol up. Now, I thought I told you the number would be between 1 and 100.')
    elif guess == 0:
        guess = True
        print('Hol up. Now, I thought I told you the number would be between 1 and 100.')
    elif guess < random_num:
        print('Not quite, gotta think BIGGER than that.')
    elif guess > random_num:
        print('Not quite, gotta think SMALLER than that.')
    else:
        guess = False
        print('You got it! And it only took you',num_guess,'guesses!')