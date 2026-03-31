class Rectangle:
    def set_width(self, width):
        self._width = width
    def set_height(self, height):
        self._height = height

class Square(Rectangle):
    def set_width(self, width):
        self._width = width
        self._height = width # Violation!
    def set_height(self, height):
        self._width = height
        self._height = height


 #LSP = Liskov Substitution Principle 
 # Square is not substituable for Rectangle because of the different behavior of set_width and set_height

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def area(self):
        return self._width * self._height

class Square(Shape):
    def __init__(self, side):
        self._side = side
    def area(self):
        return self._side * self._side
    


class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("I can fly")

class Penguin(Bird):
    def move(self):
        print("I swim, I can't fly")
