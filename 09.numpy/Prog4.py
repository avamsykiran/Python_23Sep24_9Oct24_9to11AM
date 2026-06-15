import numpy as np

def sqr(x):
    return x*x

print(sqr(4))

vectorSqr = np.frompyfunc(sqr,1,1)

a1 = np.random.randint(10,size=(4))
print(a1)
print(vectorSqr(a1))

def pw(x,y):
    return x**y

vectorPw = np.frompyfunc(pw,2,1)

a1 = np.random.randint(10,size=(4))
a2 = np.random.randint(10,size=(4))
print(a1)
print(a2)
print(vectorPw(a1,a2))

def arth(a,b):
    return a+b,a-b,a*b,a/b,a//b,a**b

vector_arth = np.frompyfunc(arth,2,6)
print(vector_arth(a1,a2))