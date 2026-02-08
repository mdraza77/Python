import random
inp = input("Roll the dice (y/n)?")
if inp == 'y' or inp == 'Y':
    random_number1 = random.randint(1, 6)
    random_number2 = random.randint(1, 6)
    print(random_number1, random_number2)
elif (inp == 'n' or inp == 'N'):
    print("Thank you!")
else:
    print("Invalid feedback!")
