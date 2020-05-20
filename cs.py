a = input()
b = input()
c = []
d = []
s = []
k = []
r1 = []
r2 = []
for i in a:
    if i in b:
        c.append(a.index(i))
print(c)

for i in b:
    if i in a:
        d.append(b.index(i))
        
print(d)
for i,j in zip(d,d[1:]):
    if j - i == 1:
        s.append(i)
        s.append(j)
s = list(sorted(set(s)))
print(s)
for i,j in zip(c,c[1:]):
    if j - i == 1:
        k.append(i)
        k.append(j)
k = list(sorted(set(k)))
print(k)
if len(s) <len(k):
    for i in s:
        r1.append(b[i])
    print(''.join(r1))
    
elif len(k) <len(s):
    for i in k:
        r2.append(a[i])
    print(''.join(r2))

        
        
       
        
    
