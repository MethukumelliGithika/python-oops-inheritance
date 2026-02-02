class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def save_to_file(self):
        with open("students.txt", "a") as file:
            file.write(f"{self.name},{self.marks}\n")

    @staticmethod
    def read_students():
        print("Student Records:")
        with open("students.txt", "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                print("Name:", name, "| Marks:", marks)


# Object creation
s1 = Student("Githika", 85)
s2 = Student("Vasavi", 78)

s1.save_to_file()
s2.save_to_file()

Student.read_students()
