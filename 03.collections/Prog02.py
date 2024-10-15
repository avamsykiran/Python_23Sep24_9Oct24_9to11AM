
lst = ['Vamsy','Arun','Dravid','Zinath','Charles','Arun','Baskar']

print(lst)
print(len(lst))
print(lst[2:4])
print(lst[:4])
print(lst[2:])

print(lst.count('Arun'))
print(lst.index('Arun'))

try:
    print(lst.index('arun'))
except:
    print("'arun' is not found")

lst[2] = 'Rahul Dravid'
print(lst)

lst.pop()
print(lst)

lst.remove('Arun')
print(lst)

lst.insert(3,'Baskar')
print(lst)

lst[2:4]=["Ravali","Manu"]
print(lst)

lst[2:4]=["Zubedha","Nayeem","Pratap"]
print(lst)

lst.sort()
print(lst)

for ele in lst:
    print("Hello {}!".format(ele))
    print("{} is the {}th element of the list".format(ele,lst.index(ele)))

print("------------------------------------------------------------")

for i in range(len(lst)):
    print("Hello {}!".format(lst[i]))
    print("{} is the {}th element of the list".format(lst[i],i))

print("------------------------------------------------------------")

#print(ele) for ele in lst

lst2 = lst.copy()
print(lst2)

lst2.extend(lst)
print(lst2)

lst2.reverse()
print(lst2)

for ele in lst:
    print("Hello {}!".format(ele))
    print("{} is the {}th element of the list".format(ele,lst.index(ele)))