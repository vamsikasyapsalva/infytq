a = 'Geeks'
b = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if len(a[i:j]) == 3:
            b.append(a[i:j])
            
print(b)
