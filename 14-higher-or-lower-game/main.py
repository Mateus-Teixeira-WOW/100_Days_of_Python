# imports
from game_data import data
import random
from art import logo


def game():
    won = True
    score = 0
    print(logo)

    while won:
        # chose celeb
        account_1 = random.choice(data)
        old_accounts = [account_1]
        account_2 = random.choice(data)
        while account_2 in old_accounts:
            account_2 = random.choice(data)
        old_accounts.append(account_2)

        # compare followers
        biggest_amount = 0
        biggest_account = {}
        for account in old_accounts:
            if account['follower_count'] > biggest_amount:
                biggest_amount = account['follower_count']
                biggest_account = account

        # User has to chose
        user_choice = input(f"""Compare A:\n{account_1['name']}
    is a {account_1['description']}, from {account_1['country']}
    \nAgainst B:
    {account_2['name']} is a {account_2['description']},
    from {account_2['country']}. Type 'A' or 'B': """)

        # see if user won and add score
        account_choice = ""
        if user_choice.lower() == "a":
            account_choice = account_1['name']
        elif user_choice.lower() == "b":
            account_choice = account_2['name']

        if account_choice == biggest_account['name']:
            won = True
            for _ in range(50):
                print("")
            print("You got it!\n")
            print("Next: \n")
            score += 1
        else:
            won = False
            for _ in range(50):
                print("")
            print("You lose.")
            print(f"Your score: {score}")

    play_again = input("Play again? 'y' or 'n': ")

    if play_again == 'y':
        game()
    else:
        for _ in range(50):
            print("")


game()
