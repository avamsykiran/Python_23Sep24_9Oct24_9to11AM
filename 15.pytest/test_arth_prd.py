from arth import prd

def testPrdIdentityCase():
    assert prd(1,10)==10
    
def testPrdNegativeCase():
    assert prd(-10,-10)==100
    
def testPrdPositiveCase():
    assert prd(10,10)==100    

def testPrdNegativeAndPositiveCase():
    assert prd(-10,10)==-100