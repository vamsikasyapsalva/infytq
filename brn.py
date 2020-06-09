a = 'gfg is [1] [4] all geeks'
b = []
for i,j,k in zip(a,a[1:],a[2:]):
    if i == '[' and j.isdigit() and k == ']':
        b.append(j)
print(b)
