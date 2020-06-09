a = 'hello#81@21349'
b = []
c = []
d = []
m = 0
e = []
for i in a:
    if i.isdigit():
        b.append(i)
b = list(map(int,b))
for i in b:
    if i % 2 == 0:
        c.append(i)
    else:
        d.append(i)
if len(c) == 0:
    print('-1')
else:
    m = min(c)
    c.remove(m)
    c = list(sorted(set(c),reverse = True))
    #print(c)
    d = list(sorted(set(d),reverse = True))
    #print(d)
    for i,j in zip(d,c):
        e.append(i)
        e.append(j)
    #print(e)
    if len(d) > len(c):
        for i in d[len(c):]:
            e.append(i)
    elif len(c) > len(d):
        for i in c[len(d):]:
            e.append(i)
    e.append(m)
    e = list(map(str,e))
    print(''.join(e))
    
    
