def is_palindrome(input):
    if input == input[::-1]:
        print(f"{input} is Palindrome")
    else:
        print(f"{input} is not Palindrome")


data = input("Enter somthing to check Palindrome or not: ")
is_palindrome(data)
