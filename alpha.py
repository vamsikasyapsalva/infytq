a = 'geeksfor23geeks is best45 for gee34ks and cs'
a = a.split()
b = []
for i in a:
    if i.isalnum() and i.isalpha() == False:
        b.append(i)
print(b)
        
