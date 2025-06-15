class Student:
    def __init__(self, first_name, last_name, age, courses, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.courses = courses
        self.pocket = 0
        self.salary = salary

    def get_fullname(self):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname
    
    def display_info(self):
        print("Name:", self.get_fullname())
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("Pocket money:", self.pocket)
        print("Salary:", self.salary)
        print("-" * 20)

student1 = Student("Alice","Pottly",20, ["Math", "English"], 10000)
student2 = Student("Bob", "Kerman",22, ["Physics", "History"], 20000)

student1.display_info()
student2.display_info()