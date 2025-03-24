# Number Guessing Game

import random

secret_number = random.randint(1,51)
number_of_guesses = 5

while True :
    user_guess = int(input("Guess a number between 1 and 50 (you have 5 attempts for correct guess!)"))
    if user_guess == secret_number :
        print("Conguratulations! you have guess the secret number 🎉🎁✨")
        print(f"Secret Number Was: {secret_number}")
        number_of_guesses -= 1
        break
    elif user_guess < secret_number and number_of_guesses > 1:
        print("Your guess is too low, try again! ")
        number_of_guesses -= 1
    elif user_guess > secret_number and number_of_guesses > 1:
        print("Your guess is too high, try again")
        number_of_guesses -= 1
    else:
        print("Sorry, You have wasted all your remaining attempts!")
        print(f"The Secret Number was {secret_number}")
        break