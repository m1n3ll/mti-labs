class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    
    def is_passed(self):
        if self.grade >= 10:
            print(f"{self.name} passed ;) ")
        else:
            print(f"{self.name} failed :( ")
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"

