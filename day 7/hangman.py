# Step 5
import random
import hangman_art
from hangman_words import word_list

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(hangman_art.logo)
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f'Pssst, the solution is {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"your guessed letter is: {guess}, this letter dont have in this word!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
