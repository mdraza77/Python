# marks = [51, 15, 45, 55, 78]
# for i in marks:
#     if i == 45:
#         continue
#     print(i)
# marks = {"name": "Md Raza", "age": 20}
# marks["village"] = "Ruhia"
# marks["village"] = "Ruhia Islampur"
# print(marks)
# for i in marks:
#     print(i)
# import math
# from math import *
# print(dir(math))
# print(sqrt(4))

# def sum(a = 3, b = 2):
#     return a+b
# print(sum())

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_data(self):
#         print("name is ", self.name, "and age is", self.age)

# s1 = Student("md raza", 50)
# print(s1.get_data())

# Encapsulation
class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def credit(self, bal):
        self.amount += bal
        print("Credited")

    def debit(self, bal):
        self.amount -= bal
        print("Debited")

    def balance(self):
        print(self.amount)
        
    @staticmethod
    def sttc():
        print(5+5)


customer1 = Bank("Md Raza", 500)
customer1.credit(200)
customer1.debit(200)
customer1.balance()
customer1.sttc()