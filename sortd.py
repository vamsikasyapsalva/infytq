a = 'Akshat 15 Nikhil 20 Akash 10'
a = a.split()
b = []
c = []
d = []
for i in a:
    if i.isdigit():
        b.append(i)
    else:
        c.append(i)
b = list(sorted(b))
c = list(sorted(c))
print(b)
print(c)
for i,j in zip(c,b):
    d.append(i)
    d.append(j)
print(' '.join(d))
