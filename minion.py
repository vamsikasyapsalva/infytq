string = 'ANANAS'
ss = []
c = []
d = []
v = ['A','E','I','O','U']
k = []
s = []
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        ss.append(string[i:j])
#print(ss)
for i in ss:
    i = list(i)
    if i[0] in v:
        k.append(''.join(i))
    else:
        s.append(''.join(i))
k1 = list(sorted(set(k)))
s1 = list(sorted(set(s)))
#print(k1)
for i in ss:
    if i in k1:
        c.append(i)
    elif i in s1:
        d.append(i)
if len(c) > len(d):
    print('Kelvin',len(c))
else:
    print('Stuart',len(d))

    
        
