from datetime import datetime

#High Order Function and lambdas

langs = ["TEL","ENG","HIN"]

greetingsMapedToLangs = {"TEL":"Namasthey","ENG":"Hello","HIN":"Namaskar"}

def greetUser(userName,greetingProvider):
    for lang in langs:
        print(f"{greetingProvider(lang)} {userName}!")

def timeBasedGreetingProvider(lang):
    h = datetime.now().hour

    morningsMapedToLangs = {"TEL":"Subhodayam","ENG":"Good Morning","HIN":"Suprabhat"}
    noonsMapedToLangs = {"TEL":"Namasthey ","ENG":"Good Noon","HIN":"Namaskar"}
    eveingsMapedToLangs = {"TEL":"SubhaSayantram","ENG":"Good Evening","HIN":"SubSandhya"}

    if 5 <= h <11:
        greeting=morningsMapedToLangs[lang]
    elif 12 <= h <= 16:
        greeting=noonsMapedToLangs[lang]
    else:
        greeting=eveingsMapedToLangs[lang]

    return greeting

greetUser("Vamsy",timeBasedGreetingProvider )

greetUser("Vamsy",lambda lang:greetingsMapedToLangs[lang] )
