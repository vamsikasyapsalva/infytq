from itertools import permutations
a = input().split(',')
b = list(permutations(a,3))
#print(b)
c = []
for i in b:
    i = list(i)
    i = ''.join(i)
    c.append(i)
c = list(sorted(set(c)))
print(max(c)+','+str(len(c)))
    
