import random

random_number = random.randint(1, 100)
while True:
    try:
        user_guessed_number = int(input("Guess the number (1-100): "))
        if random_number < user_guessed_number:
            print("Too High")
        elif random_number > user_guessed_number:
            print("Too Low")
        else:
            print("Congratulations, the number is", random_number)
            break
    except ValueError:
        print("Please Enter a valid number!")
