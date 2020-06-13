a = 'Gfg, is best : for ! Geeks ;'
b = ''
for i in a:
    if ord(i) in range(65,91):
        b += i
    elif ord(i) in range(97,123):
        b += i
    elif i == ' ':
        b += i
    
        
print(b)


    
