#!/usr/bin/python

import random
secret_number = random.randint(1,100)
guess = 0
tries = 0

print "Welcome to Flossy's Number Challenge!"
print "I am thinking of a number between 1 and 100."
print "I will give you seven tries to guess my number. Good luck Brainbox!"

while guess != secret_number and tries < 7:
    guess = input("What is your guess? ")
    if guess > secret_number:
        print "That is too high."
    elif guess < secret_number:
        print "That is too low."
    tries = tries + 1

if guess ==secret_number:
    print "Holy Cow, you guessed my number Einstein!"
else:
    print "Better luck next time wannabe."
    print "The secret number was", secret_number
