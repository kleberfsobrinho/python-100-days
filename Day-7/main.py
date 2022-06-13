import random

import hangman_word_list
import hangman_art

word_list = hangman_word_list.word_list

stages = hangman_art.stages

chosen_word = random.choice(word_list)

print(f"{hangman_art.logo}")
print(f"The solution is {chosen_word}")

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6
while not end_of_game and lives:
    guess = input("Guess a letter: ").lower()

    for i, letter in enumerate(chosen_word):
        if guess == letter:
            display[i] = letter
    
    if guess not in chosen_word:
        lives -= 1

    print(display)
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    if not lives:
        print("Game over, you lose")

