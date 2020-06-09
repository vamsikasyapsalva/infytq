a = ['gfg', '   ', ' ', 'is', '            ', 'best']
b = []
c = []
for i in a:
    for j in i:
       if ord(j)  in range(97,123):
           b.append(i)
           break
print(b)
    
