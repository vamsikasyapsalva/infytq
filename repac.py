a = 'geeksforgeeks is best for geeks'
b = 'best'
a = a.split()
c = ''
for i in a:
    if i == b:
        c += i
        a.insert(a.index(i),' ')
        a.remove(i)
        a.append(c)
        break
print(' '.join(a))
        
