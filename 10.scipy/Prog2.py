from scipy import optimize

def eqn1(x):
    return x-4

print(optimize.root(eqn1,0).x)

def eqn2(x):
    return x**2 + 12*x - 2

print(optimize.root(eqn2,0).x)

"""
Method supported to solve the minima or maxima of a curve
    'CG'
    'BFGS'
    'Newton-CG'
    'L-BFGS-B'
    'TNC'
    'COBYLA'
    'SLSQP'
""" 

def curve1(x):
    return x**2 + x  + 2

#compute the global minima or lowest point of the given curve
print(optimize.minimize(curve1,0,method="BFGS"))


