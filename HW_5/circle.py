import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def contains(self, point):
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        return distance <= self.radius


x_circle = float(input("Enter the x coordinate for the center of the circle: "))
y_circle = float(input("Enter the y coordinate for the center of the circle: "))
radius = float(input("Enter the radius of the circle: "))
circle = Circle(x_circle, y_circle, radius)

x_point = float(input("Enter the x coordinate for the point: "))
y_point = float(input("Enter the y coordinate for the point: "))
point = Point(x_point, y_point)

print(circle.contains(point))

