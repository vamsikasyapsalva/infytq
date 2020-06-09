a = '6, 5, 4, 3, 2, 1'
a = a.split(', ')
#print(a)
c = 0
for i,j in zip(a,a[1:]):
    if i > j:
        c += 1
    else:
        c -= 1
c = abs(c)
if c == len(a)-1:
    print('True')
else:
    print("False")

    
