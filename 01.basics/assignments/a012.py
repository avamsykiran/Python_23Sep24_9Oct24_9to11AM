"""
write a python script to accept 
    (a) an arth-operation like (sum/dif/prod/qut/rem)
    (b) a couple of integers
    (c) execute the enterd operation and print the result
    (d) if the entered operation is other than the exepcted then print "unknown operation"
Repeat this procedure until user enters "quit" as operation.


"""    

shall_continue = True

while shall_continue:    
    cmd = input(("Command (sum/dif/prod/qut/rem/quit) ? "))

    if cmd=="quit":
        print("App Terminated")
        shall_continue=False
    elif cmd=="sum":
        n1=int(input("Enter a number: "))
        n2=int(input("Enter another number: "))
        print("Sum is "+str(n1+n2))
    elif cmd=="dif":
        n1=int(input("Enter a number: "))
        n2=int(input("Enter another number: "))
        print("Difference is "+str(n1-n2))
    elif cmd=="prod":
        n1=int(input("Enter a number: "))
        n2=int(input("Enter another number: "))
        print("Product is "+str(n1*n2))        
    elif cmd=="qut":
        n1=int(input("Enter a number: "))
        n2=int(input("Enter another number: "))
        print("Quitiont is "+str(n1/n2))        
    elif cmd=="rem":
        n1=int(input("Enter a number: "))
        n2=int(input("Enter another number: "))
        print("Quitiont is "+str(n1%n2))                
    else:
        print("unknown operation")
