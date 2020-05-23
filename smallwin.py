a = input()
b = []
c = ''
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        b.append(a[i:j])
for i in b:
    if len(i) == len(set(a)) and len(i) == len(set(i)):
        c += i
print(c)
