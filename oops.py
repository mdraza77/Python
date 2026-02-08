# using del attribute
# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Md Raza")
# print(s1.name)
# del s1
# print(s1)

# private
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass  # __ means private

#     def reset_pass(self):
#         print(acc1.__acc_pass)


# acc1 = Account(409010510004752, "raza01")
# print(acc1.acc_no)
# print(acc1.reset_pass())

# private method and attribute
# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("Hello")

#     def welcome(self):
#         self.__hello()


# p1 = Person()
# print(p1.welcome())

# Inheritance - Single and Multilevel

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car Stopped")


# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand


# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type


# car1 = Fortuner("Electric")
# car1.start()

# Inheritance - Multiple
# class A:
#     a = "Welcome to Class A"


# class B:
#     b = "Welcome to Class B"


# class C(A, B):
#     c = "Welcome to Class C"

# c1 = C()
# print(c1.a)
# print(c1.b)
# print(c1.c)

# Super class

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car Stopped")


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()


# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# Class method
# class Person:
#     name = "anonymous"

#     # def change_name(self, name):
#     #     self.__class__.name = "Razza"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changeName("Md Raza")
# print(p1.name)
# print(Person.name)

# 1. Static method
# 2. Class method (cls)
# 3. Isinstance method (self)

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     # def calculate_percentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"


# stu1 = Student(60, 50, 50)
# print(stu1.percentage)

# stu1.phy = 50
# print(stu1.phy)
# print(stu1.percentage)