from collections import defaultdict
a = 'geeksforgeeks is indias best and bright for geeks'
a = a.split()
#print(a)
b = []
c = []
s = []
for i in a:
    b.append(i[0]+i[-1])
#print(b)


for i in a:
    c.append(i[1:-1])
#print(c)

res = defaultdict(set) 
for i,j in zip(b,c): 
    res[i].add(j) 
print(dict(res))
