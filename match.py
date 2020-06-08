a = 'geeksforgeeks is best for geeks'
a = a.split()
b = 'for'
for i in range(len(a)):
    if a[i] ==  b:
        print(int(i)+1)
        break
