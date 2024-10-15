
s="mississipPI is a river"

print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.count("s"))
print(s.count("ssi"))
print(s.count("is"))
print(s.replace("s","$"))

print("abcd123".isalnum())
print("abcd123".isalpha())
print("abcd".isalpha())
print("123".isdigit())
print("123".isnumeric())
print("123".isdecimal())

print(s.find("ssi"))
print(s.index("ssi"))
print(s.find("apple"))
#print(s.index("apple")) will raise an error

print(s.split(" "))

friends = ["Sagar","Vamsy","Komali","Sudha"]
tag = " is a friend of "
print(tag.join(friends))

s1 = "    abc   "
print(s1,len(s1))
print(s1.strip(),len(s1.strip()))

