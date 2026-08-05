from my_Abstract_class import Shape
class square(Shape):
    def __init__(self, xy):
        self.xy = xy

    def area(self):
        return self.xy ** 2

class rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2


sq1 = square(5)
print(sq1.area())
rect1 = rectangle(10,20)
print(rect1.area())

cq = Circle(2)
print(cq.area())