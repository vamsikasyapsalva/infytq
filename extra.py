a = 'geeksforgeeks is best'
b = 'fes'
c = ''
for i in a:
    if i in b:
        continue
    else:
        c += i
print(c)
