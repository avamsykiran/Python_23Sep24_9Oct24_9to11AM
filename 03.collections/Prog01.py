
tp = ('Vamsy','Arun','Dravid','Zinath','Charles','Arun','Baskar')

print(tp)
print(len(tp))
print(tp[2:4])
print(tp[:4])
print(tp[2:])

print(tp.count('Arun'))
print(tp.index('Arun'))

try:
    print(tp.index('arun'))
except:
    print("'arun' is not found")