a = '6543452345456987653234'
b = []
for i,j in zip(a,a[1:]):
    b.append(abs(int(i)-int(j)))
    
print(max(b))
