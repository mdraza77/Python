def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} is {fact}")


num = int(input("Enter number: "))
factorial(num)
