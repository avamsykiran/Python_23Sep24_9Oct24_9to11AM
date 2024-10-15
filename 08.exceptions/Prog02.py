
try:
    x = int(input("A number "))
    y = int(input("A number "))
    print(x/y)
except ZeroDivisionError:
    print("Zero is not a valid divisor")
except (ValueError,NameError):
    print("Only integers are allowed as inputs")
    
print("The app is done")