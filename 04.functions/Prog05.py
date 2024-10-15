def countFactors(n):
    factorsCount=2

    for i in range(2,n//2):
        if n%i==0:
            factorsCount+=1

    return factorsCount

def isPrim(n):
    return countFactors(n)==2

print("{} has {} factors".format(139,countFactors(139)))
print("is {} prime? {}".format(139,isPrim(139)))

print("{} has {} factors".format(169,countFactors(169)))
print("is {} prime? {}".format(169,isPrim(169)))