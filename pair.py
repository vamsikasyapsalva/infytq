a = 'geeksforgeeks'
b = []
c = []

for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if len(a[i:j]) == 2:
            b.append(a[i:j])
            
for i in b:
    i = list(i)
    i.insert(len(i)//2,'_')
    i = ''.join(i)
    c.append(i)
print(c)
    
