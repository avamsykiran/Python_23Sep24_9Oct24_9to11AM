
userName=input("Whats your name? ")

for index in range(len(userName)):
    print(userName[:index+1])

for index in range(len(userName)):
    print(userName[:len(userName)-index])
    
