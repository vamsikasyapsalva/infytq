a = input()
d = []
ld = []
for i in a:
    if i.isdigit():
        d.append(int(i))
k = list(set(d))
for i in k:
    if i % 2 == 0:
        ld.append(i)

if len(ld) == 0:
    print('-1')
else:
    m = min(ld)
    k.remove(m)
    g = list(sorted(k,reverse = True))
    g.append(m)
    g = list(map(str,g))
    print(''.join(g))
        
