import random


def password_generate(name):
    name = name.replace(' ', '')
    generated_password = '@' + name[0] + name[1::] + \
        str(random.randint(0, 9)) + str(random.randint(0, 9))
    print(
        f"Based on your full name the Password is: \n{generated_password}")


name_to_password = input("Enter Full Name: ").strip().capitalize() or "User"
password_generate(name_to_password)
