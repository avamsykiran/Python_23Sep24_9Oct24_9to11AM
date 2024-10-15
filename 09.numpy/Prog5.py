import numpy as np

a1 = np.random.randint(10,size=(4))
print(a1)
print(np.sum(a1))
print(np.cumsum(a1))

print("-----------------------------------------")
a1 = np.random.randint(10,size=(4))
a2 = np.random.randint(10,size=(4))
a3 = np.add(a1,a2)

print(a1)
print(a2)
print(a3)

print("-----------------------------------------")
def multiplyBy100(x):
    return x*100

vector_multiplyBy100 = np.frompyfunc(multiplyBy100,1,1)

a1 = np.random.rand((5))
a2 = vector_multiplyBy100(a1)

print(a1)
print(a2)
print(np.trunc(a2))
print(np.around(a2))
print(np.floor(a2))
print(np.ceil(a2))
