a = 'gfgisbest'
a = list(a)
b = [1,3,4,5,7]
c = []
for i in range(len(a)):
    if i in b:
        c.append(a[i])
    
print(''.join(c))
     
    
