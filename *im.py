a = 'geeksforgeeks'
a = list(a)
r = len(a)-1
b = '*'*r
b = list(b)
print(b)
d = []
for i,j in zip(a,b):
    d.append(i+j)
d.append(a[-1])
print(''.join(d))
