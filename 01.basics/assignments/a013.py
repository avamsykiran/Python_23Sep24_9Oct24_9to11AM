"""
write a python script to accept 
    (a) an arth-operation like (sum/dif/prod/qut/rem)
    (b) a couple of integers
    (c) execute the enterd operation and print the result
    (d) if the entered operation is other than the exepcted then print "unknown operation"
Repeat this procedure until user enters "quit" as operation.
Using match..case statement

"""    

shall_continue = True

while shall_continue:    
    cmd = input(("Command (sum/dif/prod/qut/rem/quit) ? "))

    #works in python 3.10 or above.
    match cmd:
        case "quit":
            print("App Terminated")
            shall_continue=False
        case "sum":
            n1=int(input("Enter a number: "))
            n2=int(input("Enter another number: "))
            print("Sum is "+str(n1+n2))
        case "dif":
            n1=int(input("Enter a number: "))
            n2=int(input("Enter another number: "))
            print("Difference is "+str(n1-n2))
        case "prod":
            n1=int(input("Enter a number: "))
            n2=int(input("Enter another number: "))
            print("Product is "+str(n1*n2))        
        case "qut":
            n1=int(input("Enter a number: "))
            n2=int(input("Enter another number: "))
            print("Quitiont is "+str(n1/n2))        
        case "rem":
            n1=int(input("Enter a number: "))
            n2=int(input("Enter another number: "))
            print("Quitiont is "+str(n1%n2))                
        case _:
            print("unknown operation")
