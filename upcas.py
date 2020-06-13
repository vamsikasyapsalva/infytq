a = 'GeeksforGeeks'
a = list(a)
s = 4
d = a[s].upper()
a.remove(a[s])
a.insert(s,d)
print(''.join(a))
