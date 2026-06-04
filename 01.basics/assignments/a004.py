"""
    print the list of factors and number of factors of a given number
    and as well print if its prime or composite

    say 12,
        1
        2
        3
        4
        6
        12
        number of factors = 6
        12 is composite
"""    

n = 12
no_of_factors = 2

print("Factors of "+str(n)+" are: ")
print(1)

for i in range(2,n//2):
    if n%i==0 :
        no_of_factors+=1
        print(i)

print(n)

print("Number of factors = " + str(no_of_factors))

if no_of_factors==2:
    print(str(n) + " is prime")
else:
    print(str(n) + " is composite")