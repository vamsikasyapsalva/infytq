a = 'gfg is best of geeks'
a = a.split()
b = []
for i in a:
    if len(i) % 2 != 0:
        b.append(i)
print(b)
