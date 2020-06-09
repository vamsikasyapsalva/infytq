a = 'geeks'
b = a[::-1]
#print(b)
c = []
for i in range(len(b)):
    for j in range(i+1,len(b)+1):
        c.append(b[i:j])
print(c[:len(a)])
    
