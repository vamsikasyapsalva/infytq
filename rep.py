a = 'Geeksforgeeks is best for geeks and CS'
a = a.split()
d = []
b = ["best", 'CS', 'for'] 
c = 'gfg'

for i in a:
    if i in b:
        d.append(a.index(i))
print(d)
for i in d:
    a.remove(a[i])
    a.insert(i,c)
print(' '.join(a))

    
    
