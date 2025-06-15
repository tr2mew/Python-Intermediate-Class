class Student:
    def __init__(self, first_name, last_name, age, courses, pocket):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.courses = courses
        self.pocket = pocket

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("Pocket money: ", self.pocket)
        print("-" * 20)

student1 = Student("Alice","Pottly",20, ["Math", "English"], 150)
student2 = Student("Bob", "Kerman",22, ["Physics", "History"], 200)

student1.display_info()
student2.display_info()