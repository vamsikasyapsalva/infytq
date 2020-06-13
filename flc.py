a = 'welcome to geeksforgeeks'
b = []
a = a.split()
for i in a:
    b.append(i[0].upper()+i[1:len(i)-1]+i[len(i)-1].upper())
    
print(b)
    
