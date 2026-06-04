"""
    print the multiplication table of given number until 12.
    say 3 is given the output mus tbe 
    1 x 3 = 3
    2 x 3 = 6
    ....
    12 x 3 = 36    
"""    

n = int(input("Enter a number: "))
for i in range(1,12):
    print(str(i) + " x " + str(n) + " = " + str(n*i) )
