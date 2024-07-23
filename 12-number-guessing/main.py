import random
from art import logo
from art import him


def game():
    print(logo)
    computers_number = random.randint(0, 101)
    print("Im thinking a number between 0 and 100.")
    dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
    if dificulty == 'easy':
        lifes = 10
    else:
        lifes = 5

    guess = int(input("What's your guess?"))
    should_continue = True
    while should_continue:
        if guess == computers_number:
            print("You won!")
            should_continue = False
        elif guess > computers_number:
            print("Too high.")
            lifes -= 1
            print(f"Attempts left: {lifes}")
            guess = int(input("What's your guess?"))
        elif guess < computers_number:
            print("Too low.")
            lifes -= 1
            print(f"Attempts left: {lifes}")
            guess = int(input("What's your guess?"))
        if lifes == 1:
            print("you lose.")
            print(him)
            print(computers_number)
            should_continue = False


game()
