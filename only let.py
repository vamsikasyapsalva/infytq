a = ['gfg', 'is23', 'best', 'for2', 'geeks']
b = []
c = 0
for i in a:
    c = 0
    for j in i:
        if j.isalpha():
            c += 1
    if c == len(i):
        b.append(i)
print(b)
