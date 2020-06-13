a = 'GeeksforGeeks'

b = []

for i in a:
    b.append(a.count(i))
    
d = b.index(min(b))

print(a[d])
