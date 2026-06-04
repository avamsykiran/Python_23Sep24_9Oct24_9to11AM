"""
    write a python scriopt to accept a number 'n'
    and print the first n terms of the fibnocii series

    say n is 6
        0 1 1 2 3 5 
"""    

n = int(input("Enter a number: "))

a ,b = 0, 1

print(a,end=" ")
print(b,end=" ")

for _ in range(3,n+1)
    a ,b = b , a+b
    print(b,end=" ")
    