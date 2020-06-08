a = 'geeksforgeeks, is : best for ; geeks!!'
a = list(a)
b = []
c = []
for i in a:
    if ord(i) not in range(97,123) and i != ' ' :
        b.append(a.index(i))
    else:
        c.append(i)
        
for i in b:
    c.insert(i,'*')
print(''.join(c))
