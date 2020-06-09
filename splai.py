a = 'print("geeks");'
b = a[a.index('('):]
b = list(b)
#print(b)
d = a[:a.index('(')]
b.insert(0,d)
print(b)
