
x = int(input("A number? "))
y = int(input("Another number? "))
try:
    print(x/y)
except:
    print("Zero is not a valid divisor")
print("The app is done")