# game.py
#
# Pseudo-Random numbers, input, the while loop, and the break statement
# Usage:
#      % python game.py
#
# Jeff Parker,  June 2016


import random

# Initialize random number generator
random.seed()

# Pick a number between 0 and 100
secret = random.randint(1, 99)

print("Guess my number between 0 and 100!")

count = 0
response = 0

while (response != secret):

    # Get a number from the user
    response = int(input())

    count = count + 1

    # Respond to the user
    if (response < secret):
        print("Too low! Guess again!")
    elif (response > secret):
        print("Too high! Guess again!")
    else:
        print("Lucky guess!")
        break

print("It took", count, "guesses")
