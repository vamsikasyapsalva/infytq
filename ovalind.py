a = 'geeksforgeeks'
b = []
c = ['a','e','i','o','u']
for i in range(len(a)):
    if a[i] in c:
        b.append(i)
print(b)
    
