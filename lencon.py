a = input()
b = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if len(set(a[i:j])) != len(a[i:j]) and len(set(a[i:j])) == 1:
            b.append(a[i:j])
            
print(len(max(b)))
