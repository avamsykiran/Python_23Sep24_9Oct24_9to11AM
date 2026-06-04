"""
    print the sum of the first n even numbers for a given n
    say 7,  
    12

    print the sum of the first n odd numbers for a given n
    say 7,  
    16
"""    

n=6
sum=0

"""
for i in range(1,n+1):
    if i$2==0:
        sum+=i
"""

for i in range(2,n+1,2):
    sum+=i

print(sum)

sum=0

"""
for i in range(1,n+1):
    if i$2==1: 
        sum+=i
"""

for i in range(1,n+1,2):
    sum+=i

print(sum)