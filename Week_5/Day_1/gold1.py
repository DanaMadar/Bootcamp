import math


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return self.radius/2 * math.pi

    def area(self):
        return self.radius**2 * math.pi

    def definition(self):
        print("A circle is a plane figure bounded by one...")


circle = Circle()
print(circle.radius)
print(circle.area())
print(circle.perimeter())
circle.definition()
