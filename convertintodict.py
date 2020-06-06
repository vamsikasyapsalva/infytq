a = 'gfg:1, is:2, best:3'
a = a.split(',')
print(a)
k = []
v = []
for i in a:
    i = i.split(':')
    k.append(i[0])
    v.append(i[1])
print(k)
print(v)
d = dict(zip(k,v))
print(d)
