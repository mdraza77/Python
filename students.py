class Student:
    students = []

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    @classmethod
    def add_student(cls, name="Md Raza", roll_number=21, marks=0):
        student = cls(name, roll_number, marks)
        cls.students.append(student)
        print(f"Name: {name}, Roll Number: {roll_number}, Marks: {marks}")

    def update_marks(self, new_marks):
        self.new_marks = new_marks

    def show_students_details(self):
        print(f"Marks for {self.name} updated to {self.marks}")

    @classmethod
    def search_by_roll(cls, roll_number):
        for i in cls.students:
            if i.roll_number == roll_number:
                return i
            return None

    @classmethod
    def show_all_students(cls):
        if not cls.students:
            print("No Students Found")
            return
        else:
            for student in cls.students:
                cls.show_students_details()

    @classmethod
    def update_student_marks(cls, roll_number):
        student = cls.search_by_roll(roll_number)
        if student:
            new_marks = int(input("Enter New Roll Numeber: "))
            student.update_marks(new_marks)
        else:
            print("Student Not Found")


def menu():
    while True:
        print("\n====================Menu====================")
        print("1. Add Student.")
        print("2. Show All Student.")
        print("3. Update Marks.")
        print("4. Exit.")

        choice = int(input("Enter choice (1-4): "))

        if choice == 1:
            name = input("Enter Name:")
            roll_number = int(input("Enter Roll:"))
            marks = int(input("Enter Marks:"))
            Student.add_student(name, roll_number, marks)
        elif choice == 2:
            Student.show_all_students()
        elif choice == 3:
            Student.update_student_marks()
        elif choice == 4:
            print("Thank You!")
            break
        else:
            print("Invalid Choice, try again!")


if __name__ == "__main__":
    menu()
