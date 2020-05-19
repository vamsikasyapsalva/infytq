a = list(map(int,input().split())
b = list(sorted(a))
#print(b)
c = []
r = 0

n1 = b[0]
n2 = b[1]
max = b[len(b)-1]
while n2 < max:
    c.append(n1)
    c.append(n2)
    n1,n2 = n2,n1+n2
print(list(sorted(set(c))))
