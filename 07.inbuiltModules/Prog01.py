from datetime import datetime

dt = datetime.now()
print(dt)

indpDay = datetime(1947,8,15)
print(indpDay)

indpDay = datetime(1947,8,15,12)
print(indpDay)

indpDay = datetime(1947,8,15,11,58,59)
print(indpDay)

print(indpDay.strftime("%a"))
print(indpDay.strftime("%A"))
print(indpDay.strftime("%d"))
print(indpDay.strftime("%D"))

print(indpDay.strftime("%w"))

print(indpDay.strftime("%b"))
print(indpDay.strftime("%B"))
print(indpDay.strftime("%m"))

print(indpDay.strftime("%y"))
print(indpDay.strftime("%Y"))
print(indpDay.strftime("%c"))
print(indpDay.strftime("%C"))

print(indpDay.strftime("%H:%M:%S"))
print(indpDay.strftime("%I:%M:%S %p"))

print(indpDay.strftime("%d-%b-%y"))
