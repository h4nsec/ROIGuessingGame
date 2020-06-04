# ROI Guessing Game
# Author: Stuart Hanson
# Date: 23/05/2020
# Contact: stuart_hanson@outlook.com

# Import random library
import random
import os

# Welcome User to the game
print("Welcome to the ROI guessing game")

# Collect user details
userName = input("Please enter your Name: ")

# Roll the die for the number of guesses
print("Rolling the Dice!")
diceRoll = random.randint(1,6)
print("You have %d Guesses: " %diceRoll)

# Random picks the number to guess
number = random.randint(1,99)

guesses = 0
win = 0
lose = 0

# Loop checks the users input against the randint and supplies a hint, or breaks if correct
while guesses < diceRoll:
    guess = int(input("Enter a number from 0 to 99: "))
    guesses += 1
    print("This is guess %d " %guesses)

    if guess > 100:
        print("Number out of range. Lose a turn")

    if guess < number:
        print("You guessed to low")

    elif guess > number:
        print("you guessed to high")

    elif guess == number:
        guesses = str(guesses)
        print("You Win! you guessed the right number in",guesses + " turns")
        win = +1
        break

# If the user cannot guess the number in time, they receive a message    
if guess !=number:
    number = str(number)
    print("You Lose. The number was: ",number)
    lose = +1



with open('statistics.txt', 'a+') as scoresWrite:
    if guess == number:
        scoresWrite.write("\n" + userName + "  | " + "WIN" + " | " + str(guesses))
    else:
        scoresWrite.write("\n" + userName + " | " + "LOSE" + " | " + str(guesses))
scoresWrite.close()

scoresRead = open('statistics.txt', 'r+')
scoresDisplay = scoresRead.read()
print(scoresDisplay)
scoresRead.close()