a = 'GFG is good'
a = a.split()
b = 1
c = 'best'

for i in a:
    if a.index(i) == b:
        a.remove(i)
        a.insert(1,c)
        
print(' '.join(a))
    
