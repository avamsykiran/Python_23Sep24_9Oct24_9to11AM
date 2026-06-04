"""
    write a python script to accept a number and print
    a triangles of numbers as below

    say n=3
        1
        12
        123

        123
        12
        1

         1
        222
       33333

       33333
        222
         1
"""    

n=int(input("Enter a number: "))

seperator = "-"*50

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

print(seperator)

for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end="")
    print("")

print(seperator)

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i*2):
        print(i,end="")
    print("")

print(seperator)

for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i*2):
        print(i,end="")
    print("")

