#Guess Your Number
#Attempts to guess the number picked by the player.

import string
import random

print("\tWelcome To The Guess Your Number Game!")
print("\nThink of a number between 1 and 10.")
print("\nI will attempt to guess your number.")
print("\nIf I guess too low, respond with Higher")
print("\nIf I guess too high, respond with Lower")
print("\nIf I guess correctly, respond with Correct\n")

looping = True
low_num = 1
high_num = 10
tries = 1

while looping:
    guess = random.randint(low_num,high_num)
    answer = input("\nAre you thinking of the number " + str(guess) + "?")

    if answer.upper() == "HIGHER":
        low_num = guess + 1
        tries = tries + 1
    elif answer.upper() == "LOWER":
        high_num = guess - 1
        tries = tries + 1
    else:
        print("Yay! That only took ", tries, "tries!\n")
        looping = False



input("\n\nPress enter to exit.")
