# Encapsulation
# class Bank:
#     def __init__(self):
#         self.__balance = 0

#     def deposite(self, amount):
#         self.__balance += amount
#         print(amount, "Credited to your account")

#     def withdrawl(self, amount):
#         self.__balance -= amount
#         print(amount, "Debited from your account")

#     def check_bal(self):
#         print("Available balance is:", self.__balance)


# customer1 = Bank()
# customer1.deposite(500)
# customer1.withdrawl(100)
# customer1.check_bal()

# Inheritance - Single

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(self.name, "makes a sound")


# class Dog(Animal):
#     def speak(self):
#         print(self.name, "barks")


# try:
#     dog = Dog("Robin")
#     dog.speak()
# except Exception as e:
#     print({e})

# Inheritance - Multiple

# class Father:
#     def skills(self):
#         print("Father: Gardening")


# class Mother:
#     def skills(self):
#         print("Mother: Cooking")


# class Son(Father, Mother):
#     def skills(self):
#         super().skills()
#         print("Son: Painting")


# son = Son()
# son.skills()

# Polymorphism - Overriding

# class Animal:
#     def sound(self):
#         print("Animal soun")


# class Dog(Animal):
#     def sound(self):
#         print("Dog Bark")


# dog = Dog()
# dog.sound()

# Polymorphism - Overloading

# Abstraction

# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass


# class Ractangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# try:
#     rect = Ractangle(5, 3)
#     print(rect.area())
# except Exception as e:
#     print("Error", e)

class example:
    def add(self, a, b):
        x = a+b
        return x

    def add(self, a, b, c):
        x = a+b+c
        return x


obj = example()

print(obj.add(10, 20, 30))
print(obj.add(10, 20))
