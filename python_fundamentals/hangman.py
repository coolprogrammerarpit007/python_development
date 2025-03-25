# Hangman Game

import random
words = ("apple","orange","banana","coconut","pineapple")

# dictionary
hangman_art = {
    0:("   ",
       "   ",
       "   "),
    1:(" o ",
       "   ",
       "   "),
    2:(" o ",
       " | ",
       "  "),
    3:(" o ",
       " /| ",
       "  "),
    4:(" o ",
       " /|\\ ",
       "  "),
    5:(" o ",
       " /|\\ ",
       " / "),
    6:(" o ",
       " /|\\ ",
       " / \\")
               }


def display_hangman(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)



def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
     print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        if wrong_guess <= (len(hangman_art) - 1): 
            display_hangman(wrong_guess)
            display_hint(hint)
            guessed_letter = input("Enter a single letter: ").lower()
            
            if len(guessed_letter) > 1:
                print("Please enter a single letter.")
                continue

            if guessed_letter in guessed_letters:
                print("You already guessed this letter, try another one!")
                continue
            guessed_letters.add(guessed_letter)
            if guessed_letter in answer:
                for i in range(len(answer)):
                    if answer[i] == guessed_letter:
                        hint[i] = guessed_letter

                    elif "_" not in hint:
                        display_hangman(wrong_guess)
                        display_answer(answer)
                        print("You won!")
                        is_running = False

            else:
                wrong_guess += 1
                if wrong_guess <= (len(hangman_art) - 1):
                    guessed_letters.add(guessed_letter)
                    display_hangman(wrong_guess)
                    display_hint(hint)
                else:
                    wrong_guess = 6
                    display_hangman(wrong_guess)
                    display_answer(answer)
                    print("Sorry, You lose the game!")
                    is_running = False

if __name__ == "__main__":
    main()  