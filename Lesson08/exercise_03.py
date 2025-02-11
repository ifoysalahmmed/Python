# Qs.
# Define a Circle class to create a cicle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area: {3.1416 * self.radius**2:.2f}"

    def perimeter(self):
        return f"Perimeter: {2 * 3.1416 * self.radius:.2f}"


c1 = Circle(5)
print(c1.area())
print(c1.perimeter())
