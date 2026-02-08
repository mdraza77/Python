import random

while True:
    choice = input("Roll the dice (y/n)?").lower()
    if (choice == 'y'):
        random_number1 = random.randint(1, 6)
        random_number2 = random.randint(1, 6)
        print(random_number1, random_number2)
    elif (choice == 'n'):
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
