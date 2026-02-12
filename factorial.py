def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


num = int(input("Enter number: ")) or 5
print(factorial(num))
