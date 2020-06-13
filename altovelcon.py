a = 'gaeifgsbou'
a = list(a)
b = []
c = []
r = []
v = ['a','e','i','o','u']
for i in a:
    if i in v:
        b.append(i)
    else:
        c.append(i)
for i,j in zip(b,c):
    r.append(i)
    r.append(j)
print(''.join(r))
