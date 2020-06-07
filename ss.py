import re
a = 'geeksforgeeks is best for geeks'
b = '..r'
r = re.compile(b)
c = r.search(a)
print(c.group())
    
