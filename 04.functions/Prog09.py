from datetime import datetime

#High Order Function and lambdas

def greetUser(userName,greetingProvider):
    print(f"{greetingProvider()} {userName}!")

def timeBasedGreetingProvider():
    h = datetime.now().hour

    if 5 <= h <11:
        greeting="Good Morning"
    elif 12 <= h <= 16:
        greeting="Good Noon"
    else:
        greeting="Good Evening"

    return greeting

greetUser("Vamsy",timeBasedGreetingProvider )

greetUser("Vamsy",lambda: "Hello" )
greetUser("Vamsy",lambda: "Namasthey" )
greetUser("Vamsy",lambda: "Namaskar" )
greetUser("Vamsy",lambda: "Vanakkam" )
