a = 'gfg is best for geeks'
k = 7
c = ''
for i in a[k:]:
    if i == ' ':
        break
    else:
        c += i
print(c)
