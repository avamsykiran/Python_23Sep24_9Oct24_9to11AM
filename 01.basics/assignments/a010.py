"""
    print the first 12 multiples of a given number n
    say 5
        5
        10
        15
        ...
        60
"""    

n= int(input("Enter a number: "))

for i in range(1,12):
    print(n*i, end=", ")

