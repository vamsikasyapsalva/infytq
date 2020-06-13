a = input()
a = a.split(', ')
k = a[0]
l = len(a[0])
c = 0
#print(a)
b = []
for i,j in zip(k,k[::-1]):
    s = k[k.index(j):]+k[:k.index(j)]
    c += 1
    if s == a[1]:
        print(c)
        break
