"""
    write a python scriopt to accept three numbers a, n and d
    and print the first n terms of the following series

    say a = 1
        d = 2
        n = 5
        
        1 3 5 7 9
"""    

n = int(input("Enter a number: "))
a = int(input("Enter inital value: "))
d = int(input("Enter distence: "))

print(a,end=" ")

"""
for i in range(2,n+1):
    print((a+(i*d)),end=" ")

"""

for _ in range(2,n+1):
    a += d
    print(a,end=" ")