a = input()
b = []
for i in range(len(a)):
    if i % 2!=0:
        b.append(int(a[i])*int(a[i]))
b = list(map(str,b))
print(''.join(b))

    

    
