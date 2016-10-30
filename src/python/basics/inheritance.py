# declare interface from abstract methods
from abc import ABCMeta, abstractmethod

# Interface
class Shape(metaclass = ABCMeta): # this class cannot be instantiated

    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self):pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # call super class constuctor
        super(Rectangle, self).__init__()

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return self.width + self.height

'''
hierarchy

object
  Shape
    Rectangle

'''
rect = Rectangle(5, 6)
print(rect.area())

