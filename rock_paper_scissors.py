import random

choices = ("r", "p", "s")


def get_user_choices():
    while True:
        user_choice = input("Rock Paper or Scissors (r/p/s): ").lower()
    if user_choice in choices:
        return user_choice
    else:
        print("Invalid Choice!")


def display_choices(user_choice, computer_choice):
    print("Your choice is", user_choice)
    print("Computer choice is", computer_choice)


def choose_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "s" and computer_choice == "p")
        or (user_choice == "p" and computer_choice == "r")
    ):
        display_choices()
        print("You Win")
    else:
        display_choices()
        print("Computer Win")


def play_game():
    while True:
        user_choice = get_user_choices()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        choose_winner(user_choice, computer_choice)

        play_again = input("Play Again? (y/n): ")
        if play_again == "n":
            break


play_game()
