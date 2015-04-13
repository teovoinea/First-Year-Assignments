from math import pi
class Shape:
    def set_origin(self, x, y):
        self.x, self.y = x, y
    def move(self, dx, dy):
        """Move by dx and dy"""
        self.x, self.y = self.x + dx, self.y + dy

class Line(Shape):
    def __init__(self, x, y, u, v):
        """Line with start point (x, y) and end point (u, v)"""
        Shape.set_origin(self, x, y)
        self.u, self.v = u, v
    def move(self, dx, dy):
        Shape.move(self, dx, dy)
        self.u, self.v = self.u + dx, self.v + dy
    def __str__(self):
        return "Line from (" + str(self.x) + ", " + str(self.y) + \
               ") to (" + str(self.u) + ", " + str(self.v) + ")"
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        """Rectangle at (x, y) with width w and height h"""
        Shape.set_origin(self, x, y)
        self.w, self.h = w, h
    def __str__(self):
        return "Rectangle at (" + str(self.x) + ", " + str(self.y) + \
               "), width " + str(self.w) + ", height " + str(self.h)
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, x, y, r):
        Shape.set_origin(self, x, y)
        self.r = r
    def __str__(self):
        return "Circle at (" + str(self.x) + ", " + str(self.y) + \
            "), radius " + str(self.r)
    def area(self):
        return self.r * self.r * pi

class Group:
    def __init__(self):
        self.c = set()
    def add(self, s):
        """Add shape s to group"""
        self.c = self.c | {s}
    def move(self, dx, dy):
        """Move by dx and dy"""
        for s in self.c:
            s.move(dx, dy)
    def __str__(self):
        r = "Shape with:"
        for s in self.c:
            r = r + "\n  " + str(s)
        return r
    def area(self):
        r = 0
        for s in self.c:
            r = r + s.area()
        return r
