a = 'geeksforgeeks is best'
b = [2, 4, 7, 10]
c = ''
for i in range(len(a)):
    if i in b:
        c += '*'
        
    else:
        c += a[i]
print(c)
        
