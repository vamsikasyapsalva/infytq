a = ['geeksforgeeks', 'is', 'best', 'for', 'geeks']

b = 'geeks'
c = []

j,k = 0,5

for i in a:
    if i[j:k] == b:
        c.append(i)
        
print(c)
