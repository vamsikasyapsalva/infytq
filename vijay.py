a = 'abcdcabbe'
b = []
c = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        b.append(a[i:j])
#print(b)
for i in b:
    i = list(i)
    if len(i) == len(list(set(i))):
        c.append(i)
        
d = max(c,key = len)
print(''.join(d))
        
