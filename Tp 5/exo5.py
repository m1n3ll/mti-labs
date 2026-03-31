import copy #module for shallow and deep copy
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)



original = Circle(5)

shallow = copy.copy(original)
deep = copy.deepcopy(original)

class ShapeFactory:
    _prototypes = {}

    def register_shape(cls, name, shape):
        cls._prototypes[name] = shape

    def create_shape(cls, name):
        return cls._prototypes[name].clone()
