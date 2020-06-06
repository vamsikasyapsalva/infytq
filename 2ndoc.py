a = 'Gfg is best . Gfg also has Classes now. Classes help understand better.'

a = a.split()
b = {'Gfg' :  'It', 'Classes' : 'They' } 
c = []
d = []
for i in a:
    if a.count(i) > 1:
        c.append(i)
        
c = list(sorted(set(c)))
print(c)
for i in range(len(a)):
    if a[i] in c:
        d.append(i)
print(d)
for i,j in zip(d[1:],d[2:]):
    if a[i] != a[j]:
        d.remove(j)
d = d[1:]
print(d)
for i in range(len(a)):
    if i in d:
        for j,k in b.items():
            if a[i] == j:
                a[i] = k
print(' '.join(a))
