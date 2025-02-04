
def div():
    try:
        x = int(input("A number "))
        y = int(input("A number "))
        return x/y
    except ZeroDivisionError as ze:
        print(ze.__class__)
        print(ze.__cause__)
        print("Zero is not a valid divisor")
    except (ValueError,NameError):
        print("Only integers are allowed as inputs")
    finally:  
        print("The div function is complete")

print(div())
print("The app is done")