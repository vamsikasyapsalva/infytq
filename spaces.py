a = input()
b = []
c = []
d = []
e = []
f = []
for i in range(len(a)):
    if a[i] == ' ':
        b.append(i)
    else:
        c.append(a[i])
print(b)
for i in range(1,len(b)):
    b[i] -= i
    e.append(b[i])
e.insert(0,b[0])
print(e)
for i in e:
    c.insert(i,' ')
    f.append(''.join(c))
    c.remove(' ')
print(f)
    
