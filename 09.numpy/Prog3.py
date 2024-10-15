from numpy import random

a1 = random.randint(100,size=(10))
print(a1)
print("----------------------------------------------")

a2 = random.randint(100,size=(5,5))
print(a2)
print("----------------------------------------------")

a3 = random.randint(100,size=(2,4,5))
print(a3)

print("----------------------------------------------")
random.shuffle(a1)
print(a1)
print("----------------------------------------------")
random.shuffle(a1)
print(a1)
print("----------------------------------------------")
print(random.permutation(a1))
print("----------------------------------------------")
print(random.permutation(a1))

print("----------------------------------------------")
print(random.choice(a1))
print("----------------------------------------------")
print(random.choice(a1))
print("----------------------------------------------")
print(random.choice(a1,size=(2,3)))
print("----------------------------------------------")
print(random.choice(a1,size=(2,3),p=[0.5,0,0,0.2,0,0.2,0,0,0,0.1]))
