a = 'gfg, is, best'
b = 'for, all, geeks'
a = a.split(', ')
b = b.split(', ')
c = []
for i in a:
    for j in b:
        c.append(i+j)
print(c)
