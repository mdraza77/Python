class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role:",
              self.role, "Department:", self.department, "Salary:", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 75000)


eng1 = Engineer("Md Raza", 20)
eng1.showDetails()

# emp1 = Employee("Web Developer", "Technical", 25000)
# emp1.showDetails()

# emp2 = Employee("App Developer", "Technical", 30000)
# emp2.showDetails()
