a = '010101'
b = '101101'
c = 0
for i,j in zip(a,b):
    if i == j:
        c += 1
        
print(c)
