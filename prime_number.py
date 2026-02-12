def is_prme(num):
    if num < 2:
        print("Not Prime")

    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime Number")


num = int(input("Enter number: "))
is_prme(num)
