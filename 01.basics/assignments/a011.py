"""
write a python script to accept a number from the end-user
and print its reverse and print if it is a pallendrome or not

"""    

n = int(input("Enter a number: "))

rev = 0

i = n

while i>0:
    rev = (rev*10) + (i%10)
    i = i//10

print("Reverse is: "+str(rev)) 

print(str(n) + " is " + ("NOT A " if n!=rev else " A ") + "PALLENDROME")