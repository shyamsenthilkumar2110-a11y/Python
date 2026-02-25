import random

class Person:
    """Base class demonstrating Encapsulation and Abstraction."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._id = random.randint(1000, 9999)  # Protected attribute

    def display_info(self):
        return f"ID: {self._id} | Name: {self.name} | Age: {self.age}"

class Student(Person):
    """Derived class demonstrating Inheritance."""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        self.courses = []

    def enroll(self, course_name):
        self.courses.append(course_name)
        print(f"[Success] {self.name} enrolled in {course_name}")

    def display_info(self):
        # Polymorphism: Overriding the base class method
        base_info = super().display_info()
        course_list = ", ".join(self.courses) if self.courses else "None"
        return f"[Student] {base_info} | Grade: {self.grade} | Courses: {course_list}"

class Teacher(Person):
    """Derived class for school staff."""
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        base_info = super().display_info()
        return f"[Teacher] {base_info} | Subject: {self.subject}"

class School:
    """Controller class to manage objects."""
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_directory(self):
        print(f"\n--- {self.school_name} Directory ---")
        print("TEACHERS:")
        for t in self.teachers: print(f"  {t.display_info()}")
        print("STUDENTS:")
        for s in self.students: print(f"  {s.display_info()}")

def main_menu():
    """Main application loop."""
    my_school = School("Python Academy")
    
    # Pre-populating data
    t1 = Teacher("Dr. Smith", 45, "Computer Science")
    s1 = Student("Alice", 20, "A")
    my_school.add_teacher(t1)
    my_school.add_student(s1)

    while True:
        print("\n" + "="*30)
        print(f" {my_school.school_name.upper()} ")
        print("="*30)
        print("1. View Directory")
        print("2. Add Student")
        print("3. Enroll Student in Course")
        print("4. Add Teacher")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5):\n ")

        if choice == '1':
            my_school.show_directory()
        elif choice == '2':
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            my_school.add_student(Student(name, age, grade))
        elif choice == '3':
            name = input("Enter student name: ")
            course = input("Enter course name: ")
            found = False
            for s in my_school.students:
                if s.name.lower() == name.lower():
                    s.enroll(course)
                    found = True
            if not found: print("Student not found.")
        elif choice == '4':
            name = input("Enter teacher name: ")
            age = input("Enter age: ")
            sub = input("Enter subject: ")
            my_school.add_teacher(Teacher(name, age, sub))
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main_menu()