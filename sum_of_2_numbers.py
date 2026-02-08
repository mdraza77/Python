class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("Sum is:", self.num1 + self.num2)

    def float_avg(self):
        print("Avg is:", (float(self.num1) + float(self.num2))/2)


inp1 = int(input("Enter first number: "))
inp2 = int(input("Enter second number: "))
sm1 = Sum(inp1, inp2)
sm1.add()
sm1.float_avg()
