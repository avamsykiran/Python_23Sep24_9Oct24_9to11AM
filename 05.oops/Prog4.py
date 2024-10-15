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
        return self.length*self.breadth*self.height

    #area method is being overriden
    def area(self):
        return 4 *(self.length*self.breadth) + 2*(self.breadth*self.height)

r1 = Rectangle(10,20)
r2 = Rectangle(5,5)
c1 = Cuboid(10,20,30)

print("r1 is {}x{} and its are is {} and perimeter is {}".format(r1.length,r1.breadth,r1.area(),r1.perimeter()))
print("is r1 a square? {}".format(r1.isSquare()))
print("r2 is {}x{} and its are is {} and perimeter is {}".format(r2.length,r2.breadth,r2.area(),r2.perimeter()))
print("is r2 a square? {}".format(r2.isSquare()))

print("c1 is {}x{}x{} and has a volume of {} and area is {}".format(c1.length,c1.breadth,c1.height,c1.volume(),c1.area()))