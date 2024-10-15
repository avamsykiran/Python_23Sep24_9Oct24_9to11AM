import arth
from shapes import Rectangle
import numericOperations as numOps
import loans

n1=int(input("A number: "))
n2=int(input("A number: "))

print(arth.sum(n1,n2))
print(arth.dif(n1,n2))
print(arth.prd(n1,n2))
print(arth.qut(n1,n2))
print(arth.rem(n1,n2))

r1 = Rectangle(n1,n2)

print("r1 is {}x{} and its are is {} and perimeter is {}".format(r1.length,r1.breadth,r1.area(),r1.perimeter()))
print("is r1 a square? {}".format(r1.isSquare()))

print("{} has {} as factors and is a {}".format(n1,numOps.factorsOf(n1),("Prime" if numOps.isPrime(n1) else "Composite")))

p = float(input("Enter the principal amount : "))
t = float(input("Enter the number of years : "))
i = float(input("Enter the rate of interest : "))

print (loans.simpleInterest(p,t,i))
print (loans.compositeInterest(p,t,i))

n = int(input("Enter number of emis: " ))
print (loans.emi(p,i,n))