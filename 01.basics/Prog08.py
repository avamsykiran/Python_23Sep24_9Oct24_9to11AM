# given a number n, print if it is a even positve/odd positve/even negative/odd negative
n=10
if n==0:
    print("0 is either postive nor negative and neither odd nor even")
elif n>0:
    if n%2==0:
        print(str(n)+"is even positive")
    else:
        print(str(n)+"is odd positive")
else:
    if n%2==0:
        print(str(n)+"is even negative")
    else:
        print(str(n)+"is odd negative")