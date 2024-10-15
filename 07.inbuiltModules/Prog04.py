import re

s = "Call me at 9052224753 or 9948016004 or 90524447753"

mobilePattern = "[1-9][0-9]{9}"

for x in re.findall(mobilePattern,s):
    print(x)

matchObj =  re.search(mobilePattern,s)
print(matchObj.pos)