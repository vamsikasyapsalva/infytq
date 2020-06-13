a = 'GeeksforGeeks'
b = []
for i in a:
    b.append(a.count(i))
c = b.index(max(b))
print(a[c])
