a = input()
b = []
c = input()
c = list(c)
d = []
e = []
f = []
k = []
s = 0
t = 0



for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        b.append(a[i:j])
        

for i in b:
    if len(i) >= len(c):
        if i[0] == c[0] and i[len(i)-1] in c:
            e.append(i)
print(e)
def fun(i):
    s = 0
    for j in str(sorted(set(i))):
        if j in list(c):
            s += 1
    if s == len(c):
        return ''.join(i)
    else:
        return ''
k = list(map(fun,e))
print(k)
for i in k:
    if i != '':
        d.append(i)
if len(c) != len(set(c)):
    for i in e:
        t = 0
        for j in i[1:len(i)-1]:
            if j in c:
                t += 1
        if t == len(c)-2:
            print(i)
else:
    print(min(d,key = len))
           
