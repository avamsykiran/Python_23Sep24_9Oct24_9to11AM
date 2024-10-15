def factorsOf(n):
    factors=[1]
    for i in range(2,(n//2)+1):
        if n%i==0:
            factors.append(i)
    factors.append(n)
    return factors

def isPrime(n):
    return len(factorsOf(n))==2


