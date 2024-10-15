class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def isSquare(self):
        return self.length==self.breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

class Cuboid(Rectangle):
    def __init__(self,length,breadth,height):
        Rectangle.__init__(self,length,breadth)
        self.height=height

    def volume(self):
        return self.area()*self.height

    def area(self):
        return 4 *(self.length*self.breadth) + 2*(self.breadth*self.height)
