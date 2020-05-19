import itertools
a = list(map(int,input.split()))
a = list(map(str,a))
s = 0
b = []
for i in a:
    i = list(i)
    i = list(map(int,i))
    b.append(i)
#print(b)
for i,j in itertools.combinations(b,2):
    if sum(i) == sum(j):
        s += 1
print(s)
    
