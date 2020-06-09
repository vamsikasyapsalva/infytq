import textwrap
a = 'gfg+4-1is+5best-8'
b = []
for i in a:
    if  i.isalpha() == False:
        b.append(i)
b = ''.join(b)
print(textwrap.wrap(b,2))
