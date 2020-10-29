a = 'vammsiaa'


k = 0

b = []

for i in a:
    
    b.append(a.count(i))
    
print(b)

k = b.index(max(b))

print(a[k])
