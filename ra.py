a = '1, 4-6, 8-10, 11'
a = a.split(', ')
b = []
c = []
d = []
e = []
f = []
t = []
for i in a:
    i = i.split('-')
    b.append(i)
print(b)
for i in b:
    k = list(map(int,i))
    c.append(k)
print(c)
for i in c:
    if len(i) == 2:
        d.append(i)
    else:
        t.append(i)
print(d)
for i in d:
    for j in range(i[0],i[1]+1):
        e.append(j)
print(e)
print(t)
l = t.insert(1,e)
print(sum(t,[]))
