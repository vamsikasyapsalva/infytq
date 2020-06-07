a = input()
a = a.split()  
b = []
c = []
d = []
for i in a:
    i = list(set(sorted(i)))
    b.append(len(i))
print(b)
for i in a:
    c.append(len(i))
print(c)
for i,j in zip(c,b):
    d.append(int(i)-int(j))
print(d)
s = d.index(max(d))
print(a[s])
