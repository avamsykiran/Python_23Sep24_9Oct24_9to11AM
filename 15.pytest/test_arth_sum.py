from arth import sum

def testSumIdentityCase():
    assert sum(0,1)==1
    
def testSumNegativeCase():
    assert sum(-1,-1)==-2
    
def testSumPositiveCase():
    assert sum(1,1)==2    

def testSumNegativeAndPositiveCase():
    assert sum(-1,1)==0