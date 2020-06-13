a = 'gfg is best'
b = ['g', 'f', 's']
c = ''
for i in a:
    if i in b:
        c += i.swapcase()
    else:
        c += i
        
print(c)
        
