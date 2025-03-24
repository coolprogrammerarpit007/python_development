# Rock, Paper Scissors Game

import random

options = ('rock','paper','scissor')

is_playing = True
score = 0
# print(f"Random Choice: {random_choice}")

while is_playing:
    random_choice = random.choice(options)
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    if user_choice == random_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
        continue
    elif user_choice == 'rock' and random_choice == 'paper':
        print(f"Paper covers rock. {user_choice} loses. Computer wins!")
        is_playing = False
    elif user_choice == 'scissor' and random_choice == 'rock':
        print(f"Rock crushes scissor. {user_choice} loses. Computer wins!")
        is_playing = False
    elif user_choice == 'paper' and random_choice == 'scissor':
        print(f"Scissor cuts paper. {user_choice} loses. Computer wins!")
        is_playing = False
    elif user_choice == 'rock' and random_choice == 'scissor':
        print(f"Rock crushes scissor. {user_choice} wins. User wins!")
        score += 1
        continue
    elif user_choice == 'paper' and random_choice == 'rock':
        print(f"Paper covers rock. {user_choice} wins. User wins!")
        score += 1
        continue
    elif user_choice == 'scissor' and random_choice == 'paper':
        print(f"Scissor cuts paper. {user_choice} wins. User wins!")
        score += 1
        continue
    else:
        print("Invalid input. Please enter rock, paper, or scissor.")
        continue


print()
print()
print("---------------- Thankyou for playing! ---------------------")
if score > 0:
    print(f"User wins {score} times against computer.")
print("---------------- Please Come Again Later! ------------------")