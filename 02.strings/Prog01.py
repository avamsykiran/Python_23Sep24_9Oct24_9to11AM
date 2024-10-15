#a string can be used like a array

myName = "Vamsy Kiran"
str=""
for index in range(len(myName)):
    str+=myName[index]+"-"
print(str)

#slicing [lb:ub] [:ub] [lb:]
print(myName[4:8])
print(myName[4:])
print(myName[:8])
print(myName[-8:-4])