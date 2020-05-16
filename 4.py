a = input()
a = list(a)
b = []
for i in a:
    if i.isalpha():
        b.append(i)
r = list(reversed(b))
for i in a:
    if i not in r:
        r.insert(a.index(i),i)
print(''.join(r))
