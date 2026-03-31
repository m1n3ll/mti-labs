class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override area()")
    #this means that this method is mandatory in all subclasses

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Rectangle(3, 4),
    Circle(5),
    Triangle(6, 2)
]

for shape in shapes:
    print(f"Area: {shape.area()}")


#Duck typing :what matters is what an object can do, not what type it is.
#“if it quacks like a duck, it’s a duck”
def print_area(shape_like_object):
    print("Area =", shape_like_object.area())
