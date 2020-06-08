import textwrap
a = 'Geeks4Geeks'
a = list(a)
b = []
c = []
e = []
k = []
s = 0

for i in range(len(a)):
    b.append(i)
    
for i in range(len(b)):
    b.remove(i)
    for j in b:
        c.append(a[j])
    e.append(c)
        
    b.insert(i,i)
e = ''.join(e[0])
s = len(e)//len(a)
print(textwrap.wrap(e,s))
