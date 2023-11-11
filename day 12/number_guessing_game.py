from random import random


def level():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
        return 10
    else:
        return 5

def guess():
    return int(input("Make a guess: "))


def compare(guess, number):
    if guess > number:
        return "Too high."
    elif guess < number:
        return "Too low."
    else:
        return "You win!"


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = int(random() * 100)
    print(f"Pssst, the correct answer is {number}")
    guess_count = 0
    life = level()
    print(life)
    while guess_count <= life:
        if guess_count == life:
            print("You've run out of guesses, you lose.")
            return
        else:
            life_remaining = life - guess_count
            print(f"You have {life_remaining} attempts remaining to guess the number.")
            guess_number = guess()
            if guess_number > 100 or guess_number < 1:
                print("Out of range.")
                life_remaining += 1
                continue
            if guess_number == number:
                print("You win!")
                return
            print(compare(guess_number, number))
            guess_count += 1


play_game()
