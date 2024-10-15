def sum(operand1,operand2):
    return operand1+operand2

print(sum(10,20))

def qut(numerator,denominator):
    return numerator//denominator

print(qut(8,7))
print(qut(denominator=100,numerator=670))

def sumAll(*nums):
    s=0
    for n in nums:
        s+=n
    return s

print(sumAll(10,20))
print(sumAll(10,20,30,40))
print(sumAll(10,20,-10))

def composeGreeting(**info):
    greeting="Hello "
    if "title" in info.keys(): greeting += info["title"] +" "
    if "name" in info.keys(): greeting += info["name"] +"!"
    return greeting

print(composeGreeting())
print(composeGreeting(name="Vamsy Kiran"))
print(composeGreeting(name="Vamsy Kiran",title="Mr."))