# given a number n, print if it is a even positve/odd positve/even negative/odd negative
n=10
if n>0 and n%2==0:
    print(str(n)+"is Even Positive")
elif n>0 and n%2!=0:
    print(str(n)+"is Odd Positive")
elif n<0 and n%2==0:
    print(str(n)+"is Even Negative")
elif n<0 and n%2!=0:
    print(str(n)+"is Odd Negative")