a = 'gfg is best for all geeks'
a = a.split()
b = ["best", "all"]
c = []
for i in a:
    if i in b:
        continue
    else:
        c.append(i)
print(' '.join(c))
    
