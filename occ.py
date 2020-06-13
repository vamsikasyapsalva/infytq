a = 'geeksforgeeks is best for geeks'
a = list(a)
b = 'g'
c = 0
d = []
for i in range(len(a)):
    if a[i] == b:
        c += 1
        a.remove(a[i])
        a.insert(i,c)
        
a = list(map(str,a))
print(''.join(a))
        
        
