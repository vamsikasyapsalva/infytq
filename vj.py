a = 'a4k3b2'
#a = aeknbd
a = list(a)
print(a)
b = []
c = []
s = []
k = 0
for i in a:
    if i.isalpha():
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)
for i,j in zip(b,c):
    s.append(i)
    k = ord(i)+int(j)
    s.append(chr(k))
print(''.join(s))
