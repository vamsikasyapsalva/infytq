a = 'gfg is best'
b = 0
c = ''
for i in a:
    if i == ' ':
        if b == 0:
            c += i
            b += 1
        else:
            continue
    else:
        c += i
print(c)
        

        
