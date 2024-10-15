import numpy as np

#creating 0D array or a scalar
arr1 = np.array(56)
print(arr1)
print(arr1.ndim)
print(arr1.dtype)

#creating 1D array or a vector
arr2 = np.array([1,2,3,4,5])
print(arr2)
print(arr2.ndim)
print(arr2.dtype)

#creating 2D array or a matrix
arr3 = np.array([ [1,2,3,4], [5,6,7,8] ]) 
print(arr3)
print(arr3.ndim)
print(arr3.dtype)

#slicing
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[3:9])
print(arr[:5])
print(arr[5:])
print(arr[3:9:2])
print(arr[::3])

#type safty
a1 = np.array([1,2,'3',4.33,5,"6"],dtype='i')
print(a1)

#filtering
arr = np.array([1,2,3,4,5,6,7,8,9,10])
filterExp = arr%2==0
print(arr[filterExp])
print(filterExp)

#sorting and searching
arr = np.array(['Vamsy','Anand','David','Zareena','Bharat'])
print(arr)
print(np.where(arr=='David'))
print(np.where(arr=='Komal'))
arr.sort()
print(arr)
print(arr.searchsorted('David'))
print(arr.searchsorted('Komal'))



