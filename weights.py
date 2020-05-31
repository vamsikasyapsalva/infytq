s = 'aaabbbbcccddd'
s = list(s)
k = list(sorted(set(s)))
t = [9,7,8,12,5]
r = []
a = []
w = []
c = []
f = []
j = []
w = []
z = []
l = []
d = dict()
for i in range(97,123):
    a.append(chr(i))
#print(a)
for i in range(1,27):
    w.append(i)
#print(w)
d = dict(zip(a,w))
#print(d)
for i,j in d.items():
    if i in s:
        r.append(j)
r = list(sorted(r))
#print(r)
for i in k:
    c.append(s.count(i))
#print(c)
for i,j in zip(r,c):
    for s in range(j):
        f.append(i)
    
print(f)
for i in range(len(f)):
    for j in range(i+1,len(f)+1):
        z.append(f[i:j])
for i in z:
    if len(set(i)) == 1:
        l.append(sum(i))
l = list(sorted(set(l)))
for i in t:
    if i in l:
        print('YES')
    else:
        print('NO')
