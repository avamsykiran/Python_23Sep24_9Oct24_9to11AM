class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

r1 = Rectangle(10,20)
r2 = Rectangle(5,5)

print("r1 is {}x{}".format(r1.length,r1.breadth))
print("r2 is {}x{}".format(r2.length,r2.breadth))

