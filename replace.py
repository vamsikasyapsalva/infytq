a = 'geeks for geeks'
r = []
a = a.split()
c = 'geeks'
b = 'abcd'
for i in a:
    if i == c:
        i = b
        r.append(i)
    else:
        r.append(i)
print(' '.join(r))

        
