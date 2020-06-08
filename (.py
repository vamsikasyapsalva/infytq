a = 'geeks(for)geeks is (best)'
b = []
c = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
            b.append(a[i:j])
for i in b:
    if i[0] == '(' and i[len(i)-1] == ')' and i.count('(') == 1:
        c.append(i)
print(c)
            
