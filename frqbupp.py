from collections import Counter
a = ' GeEkSForGeEkS'
b = []
c = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        b.append(a[i:j])
#print(b)
for i in b:
    if i[0].isupper() and i[1:len(i)-1].islower() and i[-1].isupper():
        c.append(i[:len(i)-1])
    elif len(i) == 2 and i.isupper():
        c.append(i[0])
        
#print(c)
for i in c:
    if i == ' ':
        c.remove(i)
print(dict(Counter(c)))
