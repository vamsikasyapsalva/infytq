a = ['GFG', 'is', 'for', 'Computer', 'Science', 'learning']
b = []
c = []
k = []
for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])
b = ' '.join(b)
c = ' '.join(c)
k.append(b)
k.append(c)
print(k)
