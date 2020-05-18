a = input()
a = a.split(',')

w = []
d = []
s = []
k = 0
r = []

for i in a:
    i = i.split(':')
    w.append(i[0])
    d.append(i[1])
    
d = list(map(int,d))

def sq(s):
    k = 0
    for i in str(s):
        k += int(i)*int(i)
    return k
h = list(map(sq,d))
#print(h)
for i,j in zip(h,w):
    if i % 2 == 0:
        r.append(j[2:]+j[:2])
    else:
        r.append(j[1:]+j[0])
        
print(' '.join(r))
        
