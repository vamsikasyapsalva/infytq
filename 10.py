a = int(input())
b = input()
b = b.split(' ')
c = []
d = []
k = []
s = 0
u = []
#print(b)
for i in b:
   if b.count(i) == 1:
       c.append(i)
   else:
       d.append(i)

if len(c) == a:
    print(len(set(d)))
elif len(c) < a:
    s = a - len(c)
    k = list(sorted(d))
    #print(k)
    for i in k[s:]:
        u.append(i)
    print(len(set(u)))
elif len(c) > a:
    s = len(c)-a
    print(len(set(d))+s)
            
