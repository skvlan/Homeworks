import math



class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        angle_in_radians = math.radians(self.angle)
        return self.width * self.height * math.sin(angle_in_radians)


class Triangle(Parallelogram):

    def __init__(self, height, width, angle):
        super().__init__(0, 0, height, width, angle)   #width = a, height = b

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nTriangle: {self.width}, {self.height}, {self.angle}'

    def square(self):
        angle_in_radians = math.radians(self.angle)
        return 0.5 * self.width * self.height * math.sin(angle_in_radians)


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 20, 30, 45)
p.x
p1 = Parallelogram(1, 2, 20, 30, 45)
str(p1)

t = Triangle(5, 5, 45)
t1 = Triangle(6, 9, 60)


scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(p)
scene.add_figure(p1)
scene.add_figure(t)
scene.add_figure(t1)

scene.total_square()






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

    def __contains__(self, point):
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        return distance <= self.radius


x_circle = float(input("Enter the x coordinate for the center of the circle: "))
y_circle = float(input("Enter the y coordinate for the center of the circle: "))
radius = float(input("Enter the radius of the circle: "))
circle = Circle(x_circle, y_circle, radius)

x_point = float(input("Enter the x coordinate for the point: "))
y_point = float(input("Enter the y coordinate for the point: "))
point = Point(x_point, y_point)

print(point in circle)
