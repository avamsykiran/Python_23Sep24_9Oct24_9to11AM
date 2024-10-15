def simpleInterest(p,r,t):
     si = (p * t * r)/100
     return si

def compositeInterest(p,t,r):
    ci =  p * (pow((1 + r / 100), t)) 
    return ci
    
def emi(p,R,n):
   r = R/(12*100)
   emi = p * r * ((1+r)**n)/((1+r)**n - 1)
   return emi