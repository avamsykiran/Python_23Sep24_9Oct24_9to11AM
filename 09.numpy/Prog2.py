import numpy as np

a1 = np.array([1,2,3,4,5,6,7,8,9,10])

#copies and views
a1Copy = a1.copy()
a1View = a1.view()

print(a1.base)
print(a1Copy.base)
print(a1View.base)

#shaping
print(a1.shape)
print(a2.shape)

print(np.array_split(a1,2))
print(np.array_split(a1,3))

print(a1.reshape((5,2)))
#print(a1.reshape((2,3)))
