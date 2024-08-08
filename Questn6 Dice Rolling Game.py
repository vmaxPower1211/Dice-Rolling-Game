#Project 6
#Create	a dice rolling game
#Won’t need user input this time if you	don’t want (not	necessary)
#Think	about a	while loop maybe?
#Seems like a good place for an	IF and ELSE statement

print("--------------------------------------------------------")

import random

question = input('Would you like to play, [y/n]? ')

while question != "n":
    if question == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("Your rolled a...")
        print(die1," and ",die2)
        question = input('\nWould you like to roll again, [y/n]? ')
    else:
        print('Invalid response. Please type "y" or "n".')
        question = input('Would you like to try to roll the dice again[y/n]?\n ')        

print('Thank you for playing - Good Bye!')
