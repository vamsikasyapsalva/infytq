a = 'GEEKSFORGEEKS'
a = list(a)

k = 4
c = a[k].lower()

a.remove(a[k])
a.insert(k,c)
print(''.join(a))


        
