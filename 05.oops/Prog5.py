
class ClassA:
    def aboutMe(self):
        print("This is from classA")

    def someMethod(self):
        print("A member method of classA")

class ClassB:
    def aboutMe(self):
        print("This is from classB")

    def anotherMethod(self):
        print("Another member method of classB")

class ClassC1(ClassA,ClassB):
    pass

class ClassC2(ClassB,ClassA):
    pass

objA = ClassA()
objB = ClassB()
objC1 = ClassC1()
objC2 = ClassC2()

objA.aboutMe()
objA.someMethod()

print("---------------------------------------------------------------------------------")

objB.aboutMe()
objB.anotherMethod()

print("---------------------------------------------------------------------------------")

objC1.aboutMe()
objC1.someMethod()
objC1.anotherMethod()

print("---------------------------------------------------------------------------------")

objC2.aboutMe()
objC2.someMethod()
objC2.anotherMethod()
