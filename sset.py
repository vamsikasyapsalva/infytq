a = "geeksforgeeks"
b = 'gfkst'
c = 0
for i in b:
    if i in a:
        c += 1
if c == len(b):
    print('True')
else:
    print('False')
        
