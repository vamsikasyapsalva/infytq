a = input().split(' ')
b = input()
c = []
m = []
a = list(map(int,a))
l = a[0]
c = a[1]
b = list(b)
for i in b:
    m.append(b.count(i))
print(m)
s = max(m)
print(s+c)
