"""A number-guessing game."""

import random
# from random import function_name

print("Greetings Player! Enter below your preferred name:")

name = input()
# print(name)
print("Welcome {}! I'm thinking of a number between 1-100. Think you can guess it right on the first try?".format(name))

random_num = random.randint(1,10)
guess = True
num_guess = 0
least_guess = 100

while guess:
    try:
        guess = int(input())
    except:
        print('To reiterate, a NUMBER between 1-100. You should only be entering integers.')
        guess = True
        continue
        
    if guess == 0 or guess == '':
        print('Hol up. Now, I thought I told you the number would be between 1 and 100.')
        guess = True
    elif guess < 0 or guess > 100:
        print('Hol up. Now, I thought I told you the number would be between 1 and 100.')
    elif guess < random_num:
        print('Not quite, gotta think BIGGER than that.')
        num_guess += 1
    elif guess > random_num:
        print('Not quite, gotta think SMALLER than that.')
        num_guess += 1
    else:
        num_guess += 1
        least_guess = num_guess if num_guess < least_guess else least_guess
        print(f'You got it! And it only took you {num_guess} guesses!\nThe fastest you have guessed my number was with only {least_guess} guesses.')
        # print('You got it! And it only took you %s guesses!' % (num_guess))
        replay = input("Would you like to play again? Enter 'yes' to replay, anything else to exit: ")
        replay = True if replay.strip() == 'yes' else False
        
        if replay == True:
            print('Starting the next round.')
            random_num = random.randint(1,10)
            guess = True
            num_guess = 0
            continue
        else:            
            print('Thanks for playing!')
            guess = False
            