#!/usr/local/bin/python3
import random as r
import click  as c

'''
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

    If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
    On a player's first turn, if their guess is
        within 10 of the number, return "WARM!"
        further than 10 away from the number, return "COLD!"
    On all subsequent turns, if a guess is
        closer to the number than the previous guess return "WARMER!"
        farther from the number than the previous guess, return "COLDER!"
    When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

c.clear()

# Print Header
print('Welcome to the guessing game')
print()

# Set loop var and winning_number
cont_cond      = 0
guess_count    = 0 
prev_guess     = 0
winning_number = r.randrange(1,101)

# Populate range list
warm_range     = []
for i in range(winning_number - 10, winning_number + 11):
    warm_range.append(i)

while cont_cond == 0:

    # Get player guess 
    player_guess = int(input("Enter a number 1-100: "))

    # Validate input
    if player_guess < 1 or player_guess > 100:
        print('OUT OF BOUNDS')

    # Do guess count based results
    if guess_count == 0 and player_guess != winning_number:
        if player_guess in warm_range:
            print('WARM!')
        else:
            print('COLD!')
    elif guess_count != 0 and player_guess != winning_number:
        if abs(player_guess - winning_number) < abs(prev_guess - winning_number):
            print('Warmer')
        else:
            print('Colder')
    
    # Save previous guess
    guess_count = guess_count + 1
    prev_guess  = player_guess
    
    # finish loop if they win
    if player_guess == winning_number:
        print('YES! you have guessed correctly, it took you {} tries'.format(guess_count))
        cont_cond = 1