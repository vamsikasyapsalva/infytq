a = input()
b = []
c = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if len(a[i:j]) == 2:
            b.append(a[i:j])
b = list(sorted(set(b)))
print(b)
for i in b:
    c.append(a.count(i))
print(c)
d = dict(sorted(zip(b,c),reverse = True))
print(d)
    
