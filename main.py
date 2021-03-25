#!/usr/local/bin/python3
# ------------------------------------------------------------------------------
import logging
from art import logo
from random import randint

#logging.basicConfig(level = logging.DEBUG)

HARD_GUESSES = 5
EASY_GUESSES = 10


def set_difficulty( level ):
    if level == 'e':
        return 10
    else:
        return 5


def check_answer( guess, secret, turns ):
    if guess < secret:
        print("too low ... ", end='')
        return turns - 1
    if guess > secret:
        print("too high ... ", end='')
        return turns - 1
    else:
        print(f"solved. You found {secret} ")


def main():
    print(logo)
    level = input("Do you want a (h)ard or (e)asy game?\n  > ").lower()[:1]
    turns = set_difficulty(level)
    print(
            "Welcome to the Number Guessing Game!\n" \
            "I'm thinking of a number between 1 and 100."
        )
    secret = randint(1, 100)
    logging.info(secret)

    guess = 0

    while guess != secret:
        guess = int(input(f"you have {turns} turns to guess my number:\n  > "))
        turns = check_answer(guess, secret, turns)

        if turns == 0:
            print(f"You ran out of turns\nthe number was {secret}")
            exit()


if __name__ == '__main__':
    main()

# logging.debug(stuff)
