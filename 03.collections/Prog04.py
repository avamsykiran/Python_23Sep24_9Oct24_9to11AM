marks = {"Math":100,"Phy":89,"Comp":100,"Chem":66}

print(marks)

print(marks.keys())
print(marks.values())

for subject in marks.keys():
    print("Score of {} is {}".format(subject,marks[subject]))

#print(marks["social"])
print(marks.get('Phy'))
print(marks.get('social'))

print(marks.setdefault('Phy',0))
print(marks.setdefault('social',0))