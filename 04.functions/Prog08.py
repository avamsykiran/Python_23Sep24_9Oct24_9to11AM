
x=107 #global variable

def f1():
    x=67    # local variable
    print(x) # we access local variable

def f2():
    print(x) # we access global variable

def f3():
    global x  # we confirm that the x being used here is not local but global x
    x=207     # the global x is being changed  
    print(x)  # we access the global variable

f1()
f2()
f3()
print(x) # we access global variable