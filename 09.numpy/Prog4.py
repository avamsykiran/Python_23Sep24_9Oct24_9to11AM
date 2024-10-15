import numpy as np

def sqr(x):
    return x*x

print(sqr(4))

vectorSqr = np.frompyfunc(sqr,1,1)

a1 = np.random.randint(10,size=(4))
print(a1)
print(vectorSqr(a1))
