friends = ["Sagar","Vamsy","Kiran","Komal","Ravi","Vishnu"]

searchFor = input("Whom do you wanna search? ")

for friend in friends:
    if friend==searchFor:
        print("He/She is found")
        break
else:
    print("He/She is not found")