class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says: Hello!"


class Teacher:
    def __init__(self, name, age, subject):
        super().__init__(name, age)  
        self.subject = subject

    def speak(self):
        return f"Teacher {self.name} says: Pay attention!"
    
    def teach(self):
        return f"{self.name} is teaching {self.subject}."




class Student:
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def speak(self):
        return f"Student {self.name} says: I love learning!"
    
    def study(self):
        return f"{self.name} is studying. Current grade: {self.grade}"
    

    # we use super because we call the parent constructor in the person class
    # Method overriding : the methods is the subclasses changes the one in the upperclass