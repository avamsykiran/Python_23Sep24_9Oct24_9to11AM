def factorial(n):
    if n==0:
        result= 1
    else:
        result= n*factorial(n-1)
    return result

print(factorial(5))

def power(x,y):
    if y==0:
        result=1
    else:
        result=x*power(x,y-1)
    return result

print(power(2,5))