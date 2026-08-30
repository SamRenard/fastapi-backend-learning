import math
from abc import ABC, abstractmethod


# Shape is now an Abstract Base Class (blueprint)
class Shape(ABC):

    @abstractmethod
    def area(self):
        # Subclasses must implement this method
        pass

    @abstractmethod
    def perimeter(self):
        # Subclasses must implement this method
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area


# --- TESTING THE CODE ---
if __name__ == "__main__":
    circle = Circle(10)
    # Using :.2f to format the output to 2 decimal places for readability
    print(f"The area of the circle: {circle.area():.2f}")
    print(f"The perimeter of the circle: {circle.perimeter():.2f}\n")

    rectangle = Rectangle(10, 20)
    print(f"The area of the rectangle: {rectangle.area()}")
    print(f"The perimeter of the rectangle: {rectangle.perimeter()}\n")

    triangle = Triangle(3, 4, 5)
    print(f"The area of the triangle: {triangle.area()}")
    print(f"The perimeter of the triangle: {triangle.perimeter()}")
